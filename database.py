import sqlite3
import datetime

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "zerog.db")

def init_db():
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
    conn = sqlite3.connect(DB_NAME, timeout=30) # Increased timeout to 30s
    conn.row_factory = sqlite3.Row
    # Enable Write-Ahead Logging for better concurrency
    conn.execute('PRAGMA journal_mode=WAL;')
    return conn

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
