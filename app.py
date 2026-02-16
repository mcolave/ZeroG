from flask import Flask, render_template, request, jsonify
from database import init_db, get_db_connection
import datetime
import os

app = Flask(__name__)

# Initialize DB on startup
init_db()

@app.route('/')
def index():
    return render_template('index.html')

from food_database import search_food_db

@app.route('/api/log', methods=['POST'])
def log_entry():
    data = request.json
    text = data.get('text', '').lower()
    
    conn = get_db_connection()
    c = conn.cursor()
    
    # Check if foods table exists
    c.execute('''CREATE TABLE IF NOT EXISTS foods (
        name TEXT PRIMARY KEY,
        carbs REAL,
        fats REAL,
        protein REAL,
        calories REAL,
        potassium REAL,
        sodium REAL DEFAULT 0,
        saturated_fat REAL DEFAULT 0,
        trans_fat REAL DEFAULT 0,
        gi REAL DEFAULT 0
    )''')
    
    # 1. Parsing logic to find food name
    # Simplistic extraction: assume the text contains a food name
    # We will try to match against known DB foods first
    
    known_foods = c.execute('SELECT * FROM foods').fetchall()
    found_food = None
    
    import re
    # Sort known foods by length
    known_foods.sort(key=lambda x: len(x['name']), reverse=True)
    
    # Check Local DB
    for food in known_foods:
        if re.search(r'\b' + re.escape(food['name']) + r'\b', text):
            found_food = dict(food)
            found_food['source'] = 'local'
            break
            
    # 2. If not in local DB, search "Online" (Simulated + Fuzzy + Real API)
    if not found_food:
        # A. Check Internal "Cloud" DB (Fast, reliable)
        # First, try to extract just the food name. This is crucial for fuzzy matching.
        # Remove numbers: "100"
        # Remove units: "grams", "g", "ml", "oz"
        # Remove prepositions/common words? Maybe too complex.
        
        # Regex to remove quantity+unit pattern
        # Handles "100g", "100 grams", "2 slices", "slices of", "slices"
        # Number is now optional: (\d+(?:\.\d+)?)?\s*
        clean_text = re.sub(r'(\d+(?:\.\d+)?)?\s*(grams|gram|g|ounces|ounce|oz|lbs|pounds|pieces|pcs|slices|slice)\b', '', text, flags=re.IGNORECASE)
        # Remove "of" if it remains at the start (e.g. " of salt")
        clean_text = re.sub(r'^\s*\b(of|in|with)\b\s*', '', clean_text, flags=re.IGNORECASE)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip() # Collapse spaces
        
        print(f"DEBUG: text='{text}', clean_text='{clean_text}'")
        
        # Try fuzzy search on cleaned text first (most likely to succeed)
        found_data = search_food_db(clean_text)
        print(f"DEBUG: search_food_db('{clean_text}') -> {found_data}")
        
        if not found_data:
             # Try raw text just in case (e.g. "apple pie" might match better as whole string if no numbers)
             found_data = search_food_db(text)
             print(f"DEBUG: search_food_db('{text}') -> {found_data}")

        if found_data:
             found_food = found_data
             found_food['name'] = clean_text if clean_text else text # Use the matched name or original
             found_food['source'] = 'internal_cloud'
        
        # B. Real External API (OpenFoodFacts) - Fallback
        if not found_food:
            try:
                import requests
                # Clean text using the SAME robust regex as above
                search_term = re.sub(r'(\d+(?:\.\d+)?)?\s*(grams|gram|g|ounces|ounce|oz|lbs|pounds|pieces|pcs|slices|slice)\b', '', text, flags=re.IGNORECASE)
                search_term = re.sub(r'^\s*\b(of|in|with)\b\s*', '', search_term, flags=re.IGNORECASE)
                search_term = re.sub(r'\s+', ' ', search_term).strip()
                
                if search_term:
                    # User-Agent is polite to set
                    headers = {'User-Agent': 'ZeroG_Nutrition_App/1.0'}
                    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={search_term}&search_simple=1&action=process&json=1"
                    r = requests.get(url, headers=headers, timeout=5) # Increased timeout
                    
                    if r.status_code == 200:
                        res = r.json()
                        products = res.get('products', [])
                        
                        # Iterate through top 5 results to find one with VALID nutrition
                        for product in products[:5]:
                            nutriments = product.get('nutriments', {})
                            cal = nutriments.get('energy-kcal_100g', 0)
                            
                            # Only accept if it has valid data (calories OR other significant macros/micros)
                            # Salt has 0 calories but high sodium. Diet Coke has 0 calories.
                            if cal > 0 or nutriments.get('sodium_100g', 0) > 0.1 or nutriments.get('carbohydrates_100g', 0) > 0 or nutriments.get('fat_100g', 0) > 0 or nutriments.get('proteins_100g', 0) > 0:
                                found_food = {
                                    'name': search_term, # Use our clean name, or product.get('product_name')
                                    'carbs': nutriments.get('carbohydrates_100g', 0),
                                    'fats': nutriments.get('fat_100g', 0),
                                    'protein': nutriments.get('proteins_100g', 0),
                                    'calories': cal,
                                    'potassium': nutriments.get('potassium_100g', 0), # Often missing/None
                                    'sodium': nutriments.get('sodium_100g', 0) * 1000, # OFF is often in g, we want mg? convert if needed. OFF usually g. 1g = 1000mg.
                                    'saturated_fat': nutriments.get('saturated-fat_100g', 0),
                                    'trans_fat': nutriments.get('trans-fat_100g', 0),
                                    'gi': 0, # OFF rarely has GI
                                    'source': 'openfoodfacts'
                                }
                                # Sanitize None values to 0
                                for k in ['carbs', 'fats', 'protein', 'potassium', 'sodium', 'saturated_fat', 'trans_fat', 'gi']:
                                    if found_food[k] is None: found_food[k] = 0
                                    
                                break # Found a good one, stop looking
                                
            except Exception as e:
                print(f"DEBUG: OpenFoodFacts failed: {e}")

        # C. Auto-Save if found in either source
        if found_food:
             try:
                 # Use the name found or the cleaned text
                 save_name = found_food['name']
                 c.execute('''INSERT INTO foods (name, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (save_name, found_food['carbs'], found_food['fats'], found_food['protein'], found_food['calories'], found_food.get('potassium', 0),
                            found_food.get('sodium', 0), found_food.get('saturated_fat', 0), found_food.get('trans_fat', 0), found_food.get('gi', 0)))
                 conn.commit()
                 print(f"DEBUG: Auto-saved {save_name} from {found_food.get('source')} to local DB")
             except Exception as e:
                 print(f"DEBUG: Could not auto-save: {e}")
                 # Try update if fail
                 pass

    if not found_food:
        # Fallback for truly unknown
        conn.close()
        return jsonify({
            'status': 'unknown', 
            'text': text,
            'debug_clean_text': locals().get('clean_text', 'N/A'),
            'debug_search_result': locals().get('found_data', 'N/A')
        })
    
    # Calculate multipliers (very basic)
    # If "2 eggs", multiplier = 2. Default = 1.
    multiplier = 1
    match = re.search(r'(\d+)', text)
    if match:
        val = float(match.group(1))
        # Heuristic: If "grams" or "g" is present immediately after number (100g) or with space (100 g)
        # Check for unit presence using regex that allows optional space
        is_gram_input = re.search(r'(\d+)\s*(grams|gram|g)\b', text, flags=re.IGNORECASE)
        
        if is_gram_input:
             # Always treat "grams" as part of 100g base
             # "100g" -> 1.0
             # "1g" -> 0.01
             multiplier = val / 100.0
        else:
             multiplier = val
        
    carbs = found_food.get('carbs', 0) * multiplier
    fats = found_food.get('fats', 0) * multiplier
    protein = found_food.get('protein', 0) * multiplier
    calories = found_food.get('calories', 0) * multiplier
    potassium = found_food.get('potassium', 0) * multiplier
    sodium = found_food.get('sodium', 0) * multiplier
    saturated_fat = found_food.get('saturated_fat', 0) * multiplier
    trans_fat = found_food.get('trans_fat', 0) * multiplier
    gi = found_food.get('gi', 0) # GI does not multiply with quantity, it's a property
    
    c.execute('''INSERT INTO logs (date, input_type, content, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (datetime.date.today().isoformat(), 'text', text, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi))
    conn.commit()
    conn.close()
    
    # Return full details for the UI popup
    scan_info = {
        'name': found_food.get('name', text),
        'qty': multiplier,
        'carbs': carbs,
        'fats': fats,
        'protein': protein,
        'calories': calories,
        'potassium': potassium,
        'sodium': sodium,
        'saturated_fat': saturated_fat,
        'trans_fat': trans_fat,
        'gi': gi,
        'source': found_food.get('source', 'unknown')
    }
    
    return jsonify({'status': 'success', 'logged': scan_info})

@app.route('/api/add_food', methods=['POST'])
def add_food():
    data = request.json
    name = data.get('name', '').lower()
    
    if not name:
        return jsonify({'status': 'error', 'message': 'Missing name'})
        
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS foods (
        name TEXT PRIMARY KEY,
        carbs REAL,
        fats REAL,
        protein REAL,
        calories REAL,
        potassium REAL
    )''')
    
    try:
        c.execute('''INSERT INTO foods (name, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (name, data.get('carbs', 0), data.get('fats', 0), 
                   data.get('protein', 0), data.get('calories', 0), 0,
                   data.get('sodium', 0), data.get('saturated_fat', 0), data.get('trans_fat', 0), data.get('gi', 0)))
        conn.commit()
    except Exception as e:
        print(f"Error adding food: {e}")
        # Maybe update if exists?
        c.execute('''UPDATE foods SET carbs=?, fats=?, protein=?, calories=? WHERE name=?''',
                  (data.get('carbs', 0), data.get('fats', 0), 
                   data.get('protein', 0), data.get('calories', 0), name))
        conn.commit()
        
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/data')
def get_data():
    conn = get_db_connection()
    
    # Get Today's Totals
    today = datetime.date.today().isoformat()
    logs = conn.execute('SELECT * FROM logs WHERE date = ? ORDER BY id DESC', (today,)).fetchall()
    
    totals = {
        'carbs': sum(l['carbs'] for l in logs),
        'fats': sum(l['fats'] for l in logs),
        'protein': sum(l['protein'] for l in logs),
        'calories': sum(l['calories'] for l in logs),
        'potassium': sum(l['potassium'] for l in logs),
        'sodium': sum(l['sodium'] for l in logs),
        'saturated_fat': sum(l['saturated_fat'] for l in logs),
        'trans_fat': sum(l['trans_fat'] for l in logs),
        # Weighted average GI? Or just not sum? Maybe max? Let's send avg for now or just 0
        'avg_gi': sum(l['gi'] for l in logs) / len(logs) if logs else 0
    }
    
    # Convert logs to list of dicts for UI
    history = [dict(row) for row in logs]
    
    # Get Settings/Targets
    settings = conn.execute('SELECT * FROM settings WHERE id = 1').fetchone()
    
    conn.close()
    
    return jsonify({
        'totals': totals,
        'targets': dict(settings),
        'history': history # Send history to frontend
    })

@app.route('/api/settings', methods=['POST'])
def update_settings():
    data = request.json
    conn = get_db_connection()
    c = conn.cursor()
    
    # Logic to adjust targets based on disease modes could go here
    # For now, just update the flags and targets if provided
    print(f"DEBUG: update_settings received: {data}")
    c.execute('''UPDATE settings SET 
                 diabetes_mode = ?, 
                 ckd_mode = ?,
                 target_carbs = ?,
                 target_fats = ?,
                 target_protein = ?,
                 target_calories = ?,
                 target_potassium = ?
                 WHERE id = 1''', 
              (data.get('diabetes_mode', 0), data.get('ckd_mode', 0),
               data.get('target_carbs', 250), data.get('target_fats', 70),
               data.get('target_protein', 100), data.get('target_calories', 2000),
               data.get('target_potassium', 3500)))
              
    conn.commit()
    conn.close()
    return jsonify({'status': 'updated'})

@app.route('/api/reset', methods=['POST'])
def reset_day():
    conn = get_db_connection()
    today = datetime.date.today().isoformat()
    conn.execute('DELETE FROM logs WHERE date = ?', (today,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'reset'})

@app.route('/api/debug_search', methods=['GET'])
def debug_search():
    query = request.args.get('q', '')
    from food_database import search_food_db
    result = search_food_db(query)
    return jsonify({'query': query, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
