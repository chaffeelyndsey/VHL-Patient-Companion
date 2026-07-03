import sqlite3
from vhl_database import DB_NAME

def view_table(table_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\n--- {table_name.upper()} ---")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    view_table("tumors")
    view_table("appointments")
    view_table("symptoms")
    view_table("medications")
