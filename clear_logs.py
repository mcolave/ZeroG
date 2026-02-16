import sqlite3
import time
import os

db_path = 'zerog.db'
print(f"Connecting to {db_path}...")

try:
    conn = sqlite3.connect(db_path, timeout=5.0) # 5 second timeout
    cursor = conn.cursor()
    
    print("Checking log count...")
    count = cursor.execute("SELECT COUNT(*) FROM logs").fetchone()[0]
    print(f"Current log count: {count}")
    
    if count > 0:
        print("Deleting logs...")
        cursor.execute("DELETE FROM logs")
        conn.commit()
        print(f"Deleted {cursor.rowcount} rows.")
    else:
        print("Logs already empty.")
        
    conn.close()
    print("Done.")

except sqlite3.OperationalError as e:
    print(f"Error: Database is locked or inaccessible. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
