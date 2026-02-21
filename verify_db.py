import sqlite3
import os
from database import DB_NAME
from food_database import FOOD_DB

def verify_macros(carbs, protein, fats, reported_calories):
    """
    Checks if macros align with reported calories using Atwater system.
    Returns (True, difference) if accurate within 15 kcal margin, else (False, difference).
    """
    calculated_cals = (carbs * 4) + (protein * 4) + (fats * 9)
    diff = reported_calories - calculated_cals
    is_accurate = abs(diff) <= 15
    return is_accurate, calculated_cals, diff

def run_verification():
    anomalies = []

    print("--- Starting ZeroG Food Database Verification ---\n")

    # 1. Check food_database.py
    print("Checking static 'food_database.py'...")
    for key, data in FOOD_DB.items():
        # Avoid missing keys error if the database has incomplete records
        carbs = data.get('carbs', 0)
        protein = data.get('protein', 0)
        fats = data.get('fats', 0)
        cals = data.get('calories', 0)
        
        is_accurate, calc_cal, diff = verify_macros(carbs, protein, fats, cals)
        if not is_accurate:
            anomalies.append({
                'source': 'food_database.py',
                'name': data.get('name', key),
                'reported_cals': cals,
                'calculated_cals': calc_cal,
                'diff': diff,
                'macros': f"C:{carbs}g P:{protein}g F:{fats}g"
            })

    # 2. Check SQLite zerog.db 'foods' table
    print("Checking dynamic SQLite 'foods' table...")
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
            
            is_accurate, calc_cal, diff = verify_macros(carbs, protein, fats, cals)
            if not is_accurate:
                anomalies.append({
                    'source': 'zerog.db (foods)',
                    'name': name,
                    'reported_cals': cals,
                    'calculated_cals': calc_cal,
                    'diff': diff,
                    'macros': f"C:{carbs}g P:{protein}g F:{fats}g"
                })
        conn.close()
    except sqlite3.OperationalError:
        print("Note: Could not access SQLite 'foods' table or it doesn't exist.")
    except Exception as e:
        print(f"Error accessing SQLite: {e}")

    # 3. Print Report
    print("\n--- Verification Report ---")
    if not anomalies:
        print("All good! All food entries appear mathematically accurate (within +/- 15 kcal margin).")
    else:
        print(f"Found {len(anomalies)} anomalous entries that failed the macro math check:\n")
        print(f"{'Source':<20} | {'Name':<35} | {'Reported Cals':<15} | {'Calc Cals':<15} | {'Difference':<12} | Macros")
        print("-" * 140)
        for a in anomalies:
            print(f"{a['source']:<20} | {a['name']:<35} | {a['reported_cals']:<15.1f} | {a['calculated_cals']:<15.1f} | {a['diff']:<12.1f} | {a['macros']}")
            
    print("\nVerification complete.")

if __name__ == "__main__":
    run_verification()
