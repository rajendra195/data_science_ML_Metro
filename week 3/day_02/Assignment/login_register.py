import sqlite3

db_name = "user_data.db"

conn = sqlite3.connect(db_name)
cur = conn.cursor()

# def create_table(table_name):
#     if table_name.exists:
#         print("Table already exists.")

