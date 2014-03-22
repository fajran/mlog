import sqlite3

def init(conn):
  c = conn.cursor()
  c.execute(
    '''CREATE TABLE IF NOT EXISTS log (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         param TEXT,
         email TEXT
       )''')

