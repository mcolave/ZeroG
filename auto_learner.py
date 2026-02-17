import sqlite3
import requests
import re
import os

# Database Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "zerog.db")
FOOD_DB_FILE = os.path.join(BASE_DIR, "food_database.py")

def clean_term(text):
    """Removes quantities and units to get the core food name."""
    # Remove numbers and units like "1 cup", "100g", "2 slices"
    text = re.sub(r'(\d+(?:\.\d+)?)?\s*(grams|gram|g|kgs|kg|oz|ounce|lb|pound|cup|cups|tsps|tsp|tbsp|tablespoon|ml|l|liter|slice|slices|piece|pieces)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*\b(of|in|with)\b\s*', '', text, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', text).strip()

def search_openfoodfacts(query):
    """Searches OpenFoodFacts for the given query."""
    print(f"Searching for: '{query}'...")
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
    headers = {'User-Agent': 'ZeroG_AutoLearner/1.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            products = data.get('products', [])
            
            for product in products[:3]: # Check top 3
                nutriments = product.get('nutriments', {})
                cal = nutriments.get('energy-kcal_100g', 0)
                
                # Basic validation: must have some data
                if cal > 0 or nutriments.get('carbohydrates_100g', 0) > 0:
                    return {
                        'name': query, # Use our clean term as key
                        'carbs': nutriments.get('carbohydrates_100g', 0),
                        'fats': nutriments.get('fat_100g', 0),
                        'protein': nutriments.get('proteins_100g', 0),
                        'calories': cal,
                        'potassium': nutriments.get('potassium_100g', 0) or 0,
                        'sodium': (nutriments.get('sodium_100g', 0) or 0) * 1000, # Convert g to mg
                        'saturated_fat': nutriments.get('saturated-fat_100g', 0) or 0,
                        'trans_fat': nutriments.get('trans-fat_100g', 0) or 0,
                        'gi': 0 # Default
                    }
    except Exception as e:
        print(f"Error searching OFF: {e}")
    return None

def append_to_food_database(food_data):
    """Appends the formatted food dictionary to food_database.py"""
    entry = f"""
    "{food_data['name']}": {{
        "name": "{food_data['name']}",
        "calories": {food_data['calories']},
        "carbs": {food_data['carbs']},
        "protein": {food_data['protein']},
        "fats": {food_data['fats']},
        "potassium": {food_data['potassium']},
        "sodium": {food_data['sodium']},
        "saturated_fat": {food_data['saturated_fat']},
        "trans_fat": {food_data['trans_fat']},
        "gi": {food_data['gi']}
    }},"""
    
    try:
        with open(FOOD_DB_FILE, 'r') as f:
            content = f.read()
        
        # Look for the closing brace of FOOD_DB. 
        # It should be the '}' before 'import difflib'
        # or we can look for the last '}' that is at the start of a line
        
        target_str = "}\n\nimport difflib"
        if target_str in content:
             new_content = content.replace(target_str, entry + "\n" + target_str)
             
             with open(FOOD_DB_FILE, 'w') as f:
                f.write(new_content)
             print(f"Successfully added '{food_data['name']}' to food_database.py")
             return True
        else:
             # Fallback: Try to find the last '}' on its own line
             # This is a bit risky but works if import difflib is moved
             matches = list(re.finditer(r'^}$', content, re.MULTILINE))
             if matches:
                 # Take the last one (assuming it closes FOOD_DB)
                 # Actually, if there are functions, they might not have '}' at start of line unless they are weirdly formatted blocks
                 # But python code usually doesn't have '}' at start of line except for dict/set closing.
                 # Let's use the one before import difflib as primary method.
                 print("Error: Could not find insertion point '}\\n\\nimport difflib'")
                 return False
             else:
                 print("Error: Could not find closing brace '}'")
                 return False
            
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False

def process_missing_foods():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    print("Checking for missing foods...")
    rows = c.execute("SELECT * FROM missing_foods").fetchall()
    
    if not rows:
        print("No missing foods found.")
        conn.close()
        return

    for row in rows:
        term = row['term']
        clean_name = clean_term(term)
        
        if not clean_name:
            print(f"Skipping empty term from '{term}'")
            continue
            
        food_data = search_openfoodfacts(clean_name)
        
        if food_data:
            print(f"Found data for '{clean_name}'! Calories: {food_data['calories']}")
            if append_to_food_database(food_data):
                # Remove from missing_foods
                c.execute("DELETE FROM missing_foods WHERE term = ?", (term,))
                conn.commit()
                print(f"Removed '{term}' from missing_foods queue.")
        else:
            print(f"Could not find data for '{clean_name}'. Keeping in queue.")
            
    conn.close()
    print("\nAuto-learning complete.")

if __name__ == "__main__":
    process_missing_foods()
