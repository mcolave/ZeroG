import sqlite3
from database import DB_NAME

def get_missing_foods():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        
        c.execute("SELECT * FROM missing_foods ORDER BY count DESC")
        rows = c.fetchall()
        
        if not rows:
            print("\nNo missing foods logged yet.")
            return

        print(f"\n{'Term':<30} | {'Count':<5} | {'Last Searched'}")
        print("-" * 60)
        for row in rows:
            print(f"{row['term']:<30} | {row['count']:<5} | {row['last_searched']}")
        print("-" * 60)
        print(f"Total entries: {len(rows)}")

    except sqlite3.OperationalError:
        print("Error: 'missing_foods' table does not exist yet.")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    get_missing_foods()
