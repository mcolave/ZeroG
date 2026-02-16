import sqlite3
from database import DB_NAME

def migrate():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    print("Checking settings table schema...")
    try:
        # Get current columns
        c.execute('PRAGMA table_info(settings)')
        columns = [row[1] for row in c.fetchall()]
        print(f"Current columns: {columns}")
        
        # Columns to add
        new_columns = {
            'target_carbs': 'REAL DEFAULT 250',
            'target_fats': 'REAL DEFAULT 70',
            'target_protein': 'REAL DEFAULT 100',
            'target_calories': 'REAL DEFAULT 2000',
            'target_potassium': 'REAL DEFAULT 3500'
        }
        
        for col, dtype in new_columns.items():
            if col not in columns:
                print(f"Adding missing column: {col}")
                try:
                    c.execute(f'ALTER TABLE settings ADD COLUMN {col} {dtype}')
                except Exception as e:
                    print(f"Error adding {col}: {e}")
            else:
                print(f"Column {col} already exists.")
                
        conn.commit()
        print("Migration complete.")
        
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
