from vhl_database import create_database, DB_NAME
import sqlite3

def insert_sample_data():
  create_database()
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  cursor.execute("""
  INSERT INTO tumors
  (organ_system, location, size_mm, date_found, last_imaging_date, physician, notes)
  VALUES (?, ?, ?, ?, ?, ?, ?)
  """, (
    "Kidney",
    "Left Kidney", 
    8.5,
    "2026-01-12",
    "2026-02-20"
    "Dr. Example"
    "Small lesion being monitored."
  ))

cursor.execute("""
    INSERT INTO appointments
    (appointment_type, date, provider, location, notes, follow_up_needed)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        "MRI",
        "2026-08-15",
        "Radiology",
        "Corewell Health",
        "Routine surveillance imaging.",
        1
    ))

    cursor.execute("""
    INSERT INTO symptoms
    (date, symptom, severity, duration, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "2026-07-01",
        "Headache",
        4,
        "2 hours",
        "Mild headache after work."
    ))

    cursor.execute("""
    INSERT INTO medications
    (medication_name, dose, frequency, start_date, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "Example Medication",
        "10 mg",
        "Once daily",
        "2026-06-01",
        "Placeholder medication record."
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_sample_data()
    print("Sample VHL Companion data added successfully.")
