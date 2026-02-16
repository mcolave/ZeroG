import re
from food_database import search_food_db

def test_logic(text):
    print(f"--- Testing: '{text}' ---")
    
    # regex from app.py
    clean_text = re.sub(r'\d+(\.\d+)?\s*(g|grams|gram|ml|oz|ounces|lbs|pounds|pieces|pcs|slice|slices)?', '', text, flags=re.IGNORECASE)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    print(f"Cleaned: '{clean_text}'")
    
    found = search_food_db(clean_text)
    print(f"Search Result: {found}")
    
    if not found:
        print("Fallback to raw text...")
        found = search_food_db(text)
        print(f"Raw Search Result: {found}")

test_logic("100g brocolli")
test_logic("brocolli")
