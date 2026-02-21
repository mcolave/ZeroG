import sqlite3
import datetime
import os

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Check for Postgres cloud database URL
DATABASE_URL = os.getenv('DATABASE_URL')
# Legacy file path fallback
RENDER_DISK = os.getenv('RENDER_DISK_PATH')
if RENDER_DISK:
    DB_NAME = os.path.join(RENDER_DISK, "zerog.db")
else:
    DB_NAME = os.path.join(BASE_DIR, "zerog.db")

class DBCursorWrapper:
    def __init__(self, cursor, is_postgres):
        self.cursor = cursor
        self.is_postgres = is_postgres
        
    def execute(self, query, args=None):
        if self.is_postgres:
            # Replace sqlite '?' placeholders with postgres '%s'
            # SQLite ON CONFLICT(term) DO UPDATE -> Postgres ON CONFLICT (term) DO UPDATE
            query = query.replace('?', '%s')
            if 'INSERT OR IGNORE INTO settings' in query:
                query = 'INSERT INTO settings (id) VALUES (1) ON CONFLICT (id) DO NOTHING'
            
            if args:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)
        else:
            if args:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)
        return self

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

class DBConnectionWrapper:
    def __init__(self, conn, is_postgres):
        self.conn = conn
        self.is_postgres = is_postgres

    def cursor(self):
        if self.is_postgres:
            return DBCursorWrapper(self.conn.cursor(cursor_factory=RealDictCursor), True)
        else:
            return DBCursorWrapper(self.conn.cursor(), False)
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
        
    def execute(self, *args, **kwargs):
        c = self.cursor()
        c.execute(*args, **kwargs)
        return c

def init_db():
    if DATABASE_URL and HAS_POSTGRES:
        print("DEBUG: Initializing PostgreSQL database schema...")
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        
        # Postgres schemas
        c.execute('''CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            date TEXT NOT NULL,
            input_type TEXT NOT NULL,
            content TEXT,
            carbs REAL,
            fats REAL,
            protein REAL,
            calories REAL,
            potassium REAL,
            sodium REAL DEFAULT 0,
            saturated_fat REAL DEFAULT 0,
            trans_fat REAL DEFAULT 0,
            gi REAL DEFAULT 0
        )''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS foods (
            name TEXT PRIMARY KEY,
            carbs REAL,
            fats REAL,
            protein REAL,
            calories REAL,
            potassium REAL,
            sodium REAL DEFAULT 0,
            saturated_fat REAL DEFAULT 0,
            trans_fat REAL DEFAULT 0,
            gi REAL DEFAULT 0
        )''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            diabetes_mode BOOLEAN DEFAULT FALSE,
            ckd_mode BOOLEAN DEFAULT FALSE,
            target_carbs REAL DEFAULT 250,
            target_fats REAL DEFAULT 70,
            target_protein REAL DEFAULT 100,
            target_calories REAL DEFAULT 2000,
            target_potassium REAL DEFAULT 3500,
            target_sodium REAL DEFAULT 2300,
            target_saturated_fat REAL DEFAULT 20,
            target_trans_fat REAL DEFAULT 0
        )''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS missing_foods (
            term TEXT PRIMARY KEY,
            count INTEGER DEFAULT 1,
            last_searched TEXT
        )''')
        
        # Initialize default settings
        c.execute('INSERT INTO settings (id) VALUES (1) ON CONFLICT (id) DO NOTHING')
        
        conn.commit()
        conn.close()
    else:
        print("DEBUG: Initializing SQLite database schema...")
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        
        # Logs table
        c.execute('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            input_type TEXT NOT NULL,
            content TEXT,
            carbs REAL,
            fats REAL,
            protein REAL,
            calories REAL,
            potassium REAL,
            sodium REAL DEFAULT 0,
            saturated_fat REAL DEFAULT 0,
            trans_fat REAL DEFAULT 0,
            gi REAL DEFAULT 0
        )''')
        
        # Foods table (Moved from app.py to prevent write-locks during read operations)
        c.execute('''CREATE TABLE IF NOT EXISTS foods (
            name TEXT PRIMARY KEY,
            carbs REAL,
            fats REAL,
            protein REAL,
            calories REAL,
            potassium REAL,
            sodium REAL DEFAULT 0,
            saturated_fat REAL DEFAULT 0,
            trans_fat REAL DEFAULT 0,
            gi REAL DEFAULT 0
        )''')

        # Migration: Add columns if they don't exist
        for col in ['sodium', 'saturated_fat', 'trans_fat', 'gi']:
            try:
                c.execute(f'ALTER TABLE logs ADD COLUMN {col} REAL DEFAULT 0')
            except sqlite3.OperationalError:
                pass # Column likely exists
        
        # Settings table (single row for user settings)
        c.execute('''CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            diabetes_mode BOOLEAN DEFAULT 0,
            ckd_mode BOOLEAN DEFAULT 0,
            target_carbs REAL DEFAULT 250,
            target_fats REAL DEFAULT 70,
            target_protein REAL DEFAULT 100,
            target_calories REAL DEFAULT 2000,
            target_potassium REAL DEFAULT 3500,
            target_sodium REAL DEFAULT 2300,
            target_saturated_fat REAL DEFAULT 20,
            target_trans_fat REAL DEFAULT 0
        )''')
        
        # Missing Foods Table (For learning)
        c.execute('''CREATE TABLE IF NOT EXISTS missing_foods (
            term TEXT PRIMARY KEY,
            count INTEGER DEFAULT 1,
            last_searched TEXT
        )''')
        
        for col, default in [('target_sodium', 2300), ('target_saturated_fat', 20), ('target_trans_fat', 0)]:
            try:
                 c.execute(f'ALTER TABLE settings ADD COLUMN {col} REAL DEFAULT {default}')
            except sqlite3.OperationalError:
                 pass

        # Initialize default settings if not exists
        c.execute('INSERT OR IGNORE INTO settings (id) VALUES (1)')
        
        conn.commit()
        conn.close()

def get_db_connection():
    if DATABASE_URL and HAS_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        return DBConnectionWrapper(conn, is_postgres=True)
    else:
        conn = sqlite3.connect(DB_NAME, timeout=30) # Increased timeout to 30s
        conn.row_factory = sqlite3.Row
        # Enable Write-Ahead Logging for better concurrency
        try:
            conn.execute('PRAGMA journal_mode=WAL;')
        except:
            pass
        return DBConnectionWrapper(conn, is_postgres=False)

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
