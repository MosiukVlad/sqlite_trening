import sqlite3

conn = sqlite3.connect('ity.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER.
               major TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER 
               )""")
