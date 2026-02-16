
import sqlite3

def dump_foods():
    try:
        conn = sqlite3.connect('zerog.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        print(f"{'Name':<30} | {'Cals':<6} | {'Sodium (mg)':<10}")
        print("-" * 50)
        
        rows = cursor.execute("SELECT name, calories, sodium FROM foods ORDER BY name").fetchall()
        
        for row in rows:
            name = row['name']
            cals = row['calories']
            sod = row['sodium']
            print(f"{name:<30} | {cals:<6} | {sod:<10}")
            
        print("-" * 50)
        print(f"Total entries: {len(rows)}")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dump_foods()
