
import sqlite3
import re
import sys
import os

# Add current directory to path so we can import app modules
sys.path.append(os.getcwd())
try:
    from food_database import search_food_db
except ImportError:
    print("Could not import food_database")

def check_schema():
    print("\n--- SCHEMA CHECK ---")
    try:
        conn = sqlite3.connect('zerog.db')
        c = conn.cursor()
        
        for table in ['foods', 'logs']:
            print(f"Table: {table}")
            try:
                c.execute(f"PRAGMA table_info({table})")
                cols = [row[1] for row in c.fetchall()]
                print(f"  Columns: {cols}")
                if 'sodium' in cols:
                    print("  [OK] Sodium column present")
                else:
                    print("  [FAIL] MISSING Sodium column")
            except Exception as e:
                print(f"  Error reading schema: {e}")
        
        print("\n--- CACHED ENTRIES FOR 'SALT' ---")
        rows = c.execute("SELECT name, calories, sodium FROM foods WHERE name LIKE '%salt%'").fetchall()
        if rows:
            for row in rows:
                print(f"  '{row[0]}': {row[1]} kcal, {row[2]} mg sod")
        else:
            print("  No entries found containing 'salt'")
            
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")

def check_parsing(text):
    print(f"\n--- PARSING CHECK: '{text}' ---")
    
    # 1. Clean Text Logic from app.py
    clean_text = re.sub(r'(\d+(?:\.\d+)?)?\s*(grams|gram|g|ounces|ounce|oz|lbs|pounds|pieces|pcs|slices|slice)\b', '', text, flags=re.IGNORECASE)
    clean_text = re.sub(r'^\s*\b(of|in|with)\b\s*', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    print(f"  Clean Text: '{clean_text}'")
    
    # 2. Multiplier Logic from app.py
    multiplier = 1
    match = re.search(r'(\d+)', text)
    if match:
        val = float(match.group(1))
        is_gram_input = re.search(r'(\d+)\s*(g|grams)\b', text)
        print(f"  Value found: {val}")
        print(f"  Is gram input: {bool(is_gram_input)}")
        
        if is_gram_input:
             multiplier = val / 100.0
             print("  Logic: val / 100.0")
        else:
             multiplier = val
             print("  Logic: val (Direct count)")
             
    print(f"  Final Multiplier: {multiplier}")
    
    # 3. Search Internal DB
    print(f"\n--- SEARCH INTERNAL DB: '{clean_text}' ---")
    try:
        res = search_food_db(clean_text)
        print(f"  Result: {res}")
    except Exception as e:
        print(f"  Search Error: {e}")

if __name__ == "__main__":
    check_schema()
    check_parsing("1 Gram Salt")
    check_parsing("1g salt")
