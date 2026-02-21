from flask import Flask, render_template, request, jsonify
from database import init_db, get_db_connection
import datetime
import os
import time
import requests # Ensure it's available
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

print("DEBUG: App initializing...")
# Initialize DB on startup
try:
    print("DEBUG: Calling init_db()...")
    init_db()
    print("DEBUG: init_db() completed.")
except Exception as e:
    print(f"CRITICAL: init_db failed: {e}")


@app.route('/')
def index():
    return render_template('index.html')

from food_database import search_food_db

@app.route('/api/log', methods=['POST'])
def log_entry():
    data = request.json
    raw_text = data.get('text', '').lower()
    
    import re
    # 1. Translate Tagalog number words to digits (to support e.g. "dalawang piraso")
    tagalog_numbers = {
        r'\bisang\b': '1', r'\bisa\b': '1', 
        r'\bdalawang\b': '2', r'\bdalawa\b': '2',
        r'\btatlong\b': '3', r'\btatlo\b': '3',
        r'\bapat na\b': '4', r'\bapat\b': '4',
        r'\blimang\b': '5', r'\blima\b': '5',
        r'\banim na\b': '6', r'\banim\b': '6',
        r'\bpitong\b': '7', r'\bpito\b': '7',
        r'\bwalong\b': '8', r'\bwalo\b': '8',
        r'\bsiyam na\b': '9', r'\bsiyam\b': '9',
        r'\bsampung\b': '10', r'\bsampu\b': '10',
        r'\bkalahating\b': '0.5', r'\bkalahati\b': '0.5'
    }
    text = raw_text
    for tg_word, digit in tagalog_numbers.items():
        text = re.sub(tg_word, digit, text, flags=re.IGNORECASE)
    
    print(f"DEBUG: Processing log entry for text: '{text}' (orig: '{raw_text}')")
    
    conn = None
    try:
        conn = get_db_connection()
        c = conn.cursor()
    
        # Check Local DB
        # Parsing logic: Simplistic extraction
        known_foods = c.execute('SELECT * FROM foods').fetchall()
        print(f"DEBUG: Loaded {len(known_foods)} local foods.")
        found_food = None
        
        import re
        # Sort known foods by length
        known_foods.sort(key=lambda x: len(x['name']), reverse=True)
        
        for food in known_foods:
            if re.search(r'\b' + re.escape(food['name']) + r'\b', text):
                found_food = dict(food)
                found_food['source'] = 'local'
                print(f"DEBUG: Found in local DB: {found_food['name']}")
                break
                
        # Close connection while doing potential network requests to avoid holding locks
        conn.close()
        conn = None 
            
        # 2. If not in local DB, search "Online" (Simulated + Fuzzy + Real API)
        if not found_food:
            print("DEBUG: Not found in local DB, trying internal cloud/API...")
            
            # Use 'search_food_db' from food_database.py (Simulated "Online")
            # Cleaning logic
            
            # Expanded units regex including Tagalog (piraso, hiwa, tasa, kutsara, kutsarita, gramo, baso, basong)
            unit_regex = r'(\d+(?:\.\d+)?)?\s*\b(grams|gram|g|ounces|ounce|oz|lbs|pounds|pieces|pcs|slices|slice|ml|milliliters|milliliter|liter|l|cup|cups|piraso|hiwa|tasa|kutsara|kutsarita|gramo|baso|basong)\b'
            # Expanded connectors regex including Tagalog (of, in, with, ng, na)
            connector_regex = r'\s*\b(of|in|with|ng|na)\b\s*'

            clean_text = text
            clean_text = re.sub(unit_regex, '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(connector_regex, '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r'\b\d+(\.\d+)?\b', '', clean_text)
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            
            print(f"DEBUG: text='{text}', clean_text='{clean_text}'")
            
            # Try fuzzy search on cleaned text first
            found_data = search_food_db(clean_text)
            print(f"DEBUG: search_food_db('{clean_text}') -> {found_data}")
            
            if not found_data:
                 found_data = search_food_db(text)
                 print(f"DEBUG: search_food_db('{text}') -> {found_data}")

            if found_data:
                 found_food = found_data
                 found_food['name'] = clean_text if clean_text else text
                 found_food['source'] = 'internal_cloud'
            
            # B. Real External API (OpenFoodFacts) - Fallback
            if not found_food:
                try:
                    import requests
                    search_term = text
                    search_term = re.sub(unit_regex, '', search_term, flags=re.IGNORECASE)
                    search_term = re.sub(connector_regex, '', search_term, flags=re.IGNORECASE)
                    search_term = re.sub(r'\b\d+(\.\d+)?\b', '', search_term)
                    search_term = re.sub(r'\s+', ' ', search_term).strip()
                    
                    if search_term:
                        print(f"DEBUG: Searching OpenFoodFacts for: '{search_term}'")
                        headers = {'User-Agent': 'ZeroG_Nutrition_App/1.0'}
                        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={search_term}&search_simple=1&action=process&json=1"
                        try:
                            # 3s timeout
                            r = requests.get(url, headers=headers, timeout=3)
                            print(f"DEBUG: OpenFoodFacts status: {r.status_code}")
                        except requests.exceptions.Timeout:
                            print("DEBUG: OpenFoodFacts timed out.")
                            r = None
                        except Exception as e:
                             print(f"DEBUG: OpenFoodFacts request failed: {e}")
                             r = None

                        if r and r.status_code == 200:
                            res = r.json()
                            products = res.get('products', [])
                            
                            # Helper to safely float cast
                            def to_float(val):
                                try:
                                    if val is None: return 0.0
                                    return float(val)
                                except (ValueError, TypeError):
                                    return 0.0

                            for product in products[:5]:
                                nutriments = product.get('nutriments', {})
                                cal = to_float(nutriments.get('energy-kcal_100g', 0))
                                
                                # Only accept if it has valid data
                                if cal > 0 or to_float(nutriments.get('sodium_100g', 0)) > 0.1 or to_float(nutriments.get('carbohydrates_100g', 0)) > 0:
                                    found_food = {
                                        'name': search_term, 
                                        'carbs': to_float(nutriments.get('carbohydrates_100g', 0)),
                                        'fats': to_float(nutriments.get('fat_100g', 0)),
                                        'protein': to_float(nutriments.get('proteins_100g', 0)),
                                        'calories': cal,
                                        'potassium': to_float(nutriments.get('potassium_100g', 0)),
                                        'sodium': to_float(nutriments.get('sodium_100g', 0)) * 1000,
                                        'saturated_fat': to_float(nutriments.get('saturated-fat_100g', 0)),
                                        'trans_fat': to_float(nutriments.get('trans-fat_100g', 0)),
                                        'gi': 0,
                                        'source': 'openfoodfacts'
                                    }
                                    for k in ['carbs', 'fats', 'protein', 'potassium', 'sodium', 'saturated_fat', 'trans_fat', 'gi']:
                                        if found_food[k] is None: found_food[k] = 0
                                    break
                except Exception as e:
                    print(f"DEBUG: OpenFoodFacts failed: {e}")

            # D. AI Fallback (Gemini)
            if not found_food:
                print("DEBUG: OpenFoodFacts failed, falling back to Gemini AI...")
                try:
                    import ai_nutrition
                    # Use the raw text to give Gemini context about quantity if possible,
                    # but mostly the AI takes `text`.
                    res = ai_nutrition.estimate_macros(text)
                    if res:
                        found_food = res
                    else:
                        ai_err_str = "ai_nutrition returned None"
                except Exception as e:
                    ai_err_str = str(e)
                    print(f"DEBUG: AI Fallback failed: {e}")

            # Re-open connection for writing if we found something or need to log missing
            conn = get_db_connection()
            c = conn.cursor()

            # C. Auto-Save if found
            if found_food:
                 try:
                     save_name = found_food['name']
                     c.execute('''INSERT OR IGNORE INTO foods (name, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (save_name, found_food['carbs'], found_food['fats'], found_food['protein'], found_food['calories'], found_food.get('potassium', 0),
                                found_food.get('sodium', 0), found_food.get('saturated_fat', 0), found_food.get('trans_fat', 0), found_food.get('gi', 0)))
                     conn.commit()
                     print(f"DEBUG: Auto-saved {save_name} from {found_food.get('source')} to local DB")
                 except Exception as e:
                     print(f"DEBUG: Could not auto-save: {e}")
                     # Ignore unique constraint errors etc
                     conn.rollback()
                     pass

        if not found_food:
            # Need connection to log missing
            if not conn:
                 conn = get_db_connection()
                 c = conn.cursor()
                 
            try:
                 term_to_log = locals().get('search_term', text).lower().strip()
                 if term_to_log:
                     c.execute('''INSERT INTO missing_foods (term, count, last_searched) 
                                  VALUES (?, 1, ?) 
                                  ON CONFLICT(term) DO UPDATE SET count = missing_foods.count + 1, last_searched = ?''', 
                               (term_to_log, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
                     conn.commit()
            except Exception as e:
                 print(f"DEBUG: Failed to log missing food: {e}")

            conn.close()
            return jsonify({
                'status': 'unknown', 
                'text': text,
                'debug_clean_text': locals().get('clean_text', 'N/A'),
                'debug_search_result': locals().get('found_data', 'N/A')
            })
        
        # Calculate multipliers
        if not conn:
             conn = get_db_connection()
             c = conn.cursor()
             
        multiplier = 1
        match = re.search(r'(\d+(?:\.\d+)?)', text)
        if match:
            val = float(match.group(1))
            regex = r'(\d+(?:\.\d+)?)\s*\b(grams|gram|g|kgs|kg|kilograms|kilogram|ml|milliliters|milliliter|liters|liter|l|cup|cups|piraso|hiwa|tasa|kutsara|kutsarita|gramo|baso|basong)\b'
            match_unit = re.search(regex, text, flags=re.IGNORECASE)
            
            if match_unit:
                 val = float(match_unit.group(1))
                 unit = match_unit.group(2).lower()
                 if unit in ['l', 'liter', 'liters', 'litro']: multiplier = val * 10
                 elif unit in ['kg', 'kgs', 'kilogram', 'kilograms', 'kilo']: multiplier = val * 10
                 elif unit in ['cup', 'cups', 'tasa', 'baso', 'basong']: multiplier = val * 2.4
                 elif unit in ['kutsara']: multiplier = val * 0.15 # tbsp ~ 15g
                 elif unit in ['kutsarita']: multiplier = val * 0.05 # tsp ~ 5g
                 elif unit in ['piraso', 'hiwa']: multiplier = val # standard 1 unit
                 else: multiplier = val / 100.0 # grams/ml default
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
        gi = found_food.get('gi', 0)
        
        c.execute('''INSERT INTO logs (date, input_type, content, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (datetime.date.today().isoformat(), 'text', text, carbs, fats, protein, calories, potassium, sodium, saturated_fat, trans_fat, gi))
        conn.commit()
        
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

    except Exception as e:
        print(f"CRITICAL ERROR in log_entry: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.route('/api/health')
def health_check():
    from food_database import search_food_db
    import os
    
    status = {'status': 'ok'}
    
    # 1. Check DB Write
    try:
        conn = get_db_connection()
        conn.execute('CREATE TABLE IF NOT EXISTS health_check (id INTEGER PRIMARY KEY)')
        conn.execute('INSERT INTO health_check DEFAULT VALUES')
        conn.commit()
        conn.close()
        status['db_write'] = 'success'
    except Exception as e:
        status['db_write'] = f'failed: {e}'
        
    # 2. Check Fuzzy Match
    try:
        res = search_food_db('longaniza')
        status['fuzzy_match_longaniza'] = res['name'] if res else 'not found'
    except Exception as e:
        status['fuzzy_match_longaniza'] = f'error: {e}'
        
    # 3. Check File
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status['db_path'] = os.path.join(base_dir, "zerog.db")
    status['db_exists'] = os.path.exists(status['db_path'])
    
    return jsonify(status)

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
        conn.rollback()
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
