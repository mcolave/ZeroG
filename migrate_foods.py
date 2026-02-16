
import sqlite3

def migrate_foods():
    try:
        conn = sqlite3.connect('zerog.db')
        c = conn.cursor()
        
        # Add columns if they don't exist
        for col in ['sodium', 'saturated_fat', 'trans_fat', 'gi']:
            try:
                print(f"Adding {col} to foods table...")
                c.execute(f'ALTER TABLE foods ADD COLUMN {col} REAL DEFAULT 0')
                print(f"Success: Added {col}")
            except sqlite3.OperationalError as e:
                print(f"Skipping {col}: {e}")
                
        conn.commit()
        conn.close()
        print("Migration complete.")
    except Exception as e:
        print(f"Migration Error: {e}")

if __name__ == "__main__":
    migrate_foods()
