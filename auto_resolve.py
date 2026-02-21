import sqlite3
import re
import time
from database import DB_NAME
from food_database import FOOD_DB
from verify_db import verify_macros
import ai_nutrition
from dotenv import load_dotenv

load_dotenv()

print("--- Starting Auto-Resolution of Anomlous Food Entries ---")

# 1. Identify anomalies
anomalies_food_db = []
anomalies_sqlite = []

for key, data in FOOD_DB.items():
    carbs = data.get('carbs', 0)
    protein = data.get('protein', 0)
    fats = data.get('fats', 0)
    cals = data.get('calories', 0)
    is_accurate, _, _ = verify_macros(carbs, protein, fats, cals)
    if not is_accurate:
        anomalies_food_db.append({'key': key, 'name': data.get('name', key)})

try:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    foods = c.execute("SELECT * FROM foods").fetchall()
    for row in foods:
        name = row['name']
        carbs = row['carbs'] or 0.0
        protein = row['protein'] or 0.0
        fats = row['fats'] or 0.0
        cals = row['calories'] or 0.0
        is_accurate, _, _ = verify_macros(carbs, protein, fats, cals)
        if not is_accurate:
            anomalies_sqlite.append(name)
    conn.close()
except:
    pass

print(f"Found {len(anomalies_food_db)} anomalies in food_database.py and {len(anomalies_sqlite)} in zerog.db")

# 2. Fix food_database.py
if anomalies_food_db:
    with open('food_database.py', 'r') as f:
        file_content = f.read()

    for anomaly in anomalies_food_db:
        key = anomaly['key']
        name = anomaly['name']
        print(f"\nProcessing {name} from food_database.py...")
        
        corrected_data = ai_nutrition.estimate_macros(name)
        time.sleep(4) # Rate limit protection
        
        if corrected_data:
             # Find the block for this key in the file and replace it.
             # This is tricky using regex, building a new block.
             
             new_block = f"""    "{key}": {{
        "name": "{corrected_data['name']}",
        "calories": {corrected_data['calories']:.1f},
        "carbs": {corrected_data['carbs']:.1f},
        "protein": {corrected_data['protein']:.1f},
        "fats": {corrected_data['fats']:.1f},
        "potassium": {corrected_data['potassium']:.1f},
        "sodium": {corrected_data['sodium']:.1f},
        "saturated_fat": {corrected_data['saturated_fat']:.1f},
        "trans_fat": {corrected_data['trans_fat']:.1f},
        "gi": {corrected_data['gi']}
    }}"""
             
             # Basic regex replace for the dictionary key block 
             # (assumes standard indentation formatting in food_database.py)
             pattern = re.compile(rf'^[ \t]*"{re.escape(key)}":\s*{{[^}}]+}}', re.MULTILINE)
             file_content = pattern.sub(new_block, file_content)
             print(f"  -> Successfully updated content for {name}")

    with open('food_database.py', 'w') as f:
         f.write(file_content)
    print("\nSaved updates to food_database.py")

# 3. Fix zerog.db (foods table)
if anomalies_sqlite:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for name in anomalies_sqlite:
        print(f"\nProcessing {name} from zerog.db...")
        corrected_data = ai_nutrition.estimate_macros(name)
        time.sleep(4) # Rate limit protection
        
        if corrected_data:
             c.execute('''
                 UPDATE foods SET 
                 carbs=?, fats=?, protein=?, calories=?, potassium=?, 
                 sodium=?, saturated_fat=?, trans_fat=?, gi=? 
                 WHERE name=?
             ''', (
                 corrected_data['carbs'], corrected_data['fats'], corrected_data['protein'], 
                 corrected_data['calories'], corrected_data['potassium'], corrected_data['sodium'], 
                 corrected_data['saturated_fat'], corrected_data['trans_fat'], corrected_data['gi'],
                 name
             ))
             print(f"  -> Successfully updated DB row for {name}")
    conn.commit()
    conn.close()
    print("\nSaved updates to zerog.db")

print("\n--- Auto-Resolution Complete ---")
