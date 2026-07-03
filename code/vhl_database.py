import sqlite3

DB_NAME = "vhl_companion.db"

def create_database():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS tumors (
    tumor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organ_system TEXT NOT NULL,
    location TEXT, 
    size_mm REAL, 
    date_found TEXT, 
    last_imaging_date TEXT, 
    physician TEXT, 
    notes TEXT
  )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    appointment_type TEXT NOT NULL, 
    date TEXT NOT NULL,
    provider TEXT,
    location TEXT, 
    notes TEXT,
    follow_up_needed INTEGER
  )
  """)


  cursor.execute("""
  CREATE TABLE IF NOT EXISTS symptoms (
    symptom_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    date TEXT NOT NULL,
    symptom TEXT NOT NULL, 
    severity INTEGER, 
    duration TEXT, 
    notes TEXT
  )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    medication_name TEXT NOT NULL, 
    dose TEXT, 
    frequency TEXT, 
    start_date TEXT, 
    notes TEXT
  )
  """)

  conn.commit()
  conn.close()

if__name__ == "__main__":
  create_database()
  print("VHL Companion database created successfully.")













  
