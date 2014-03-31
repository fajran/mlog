import sqlite3

def init(conn):
  c = conn.cursor()
  c.execute(
    '''CREATE TABLE IF NOT EXISTS email_log (
         `id` INTEGER PRIMARY KEY AUTOINCREMENT,
         `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         `param` TEXT,
         `email` TEXT,
         `stage` INTEGER DEFAULT 0,
         `sender` TEXT,
         `receiver` TEXT,
         `subject` TEXT,
         `date_raw` TEXT,
         `message_id` TEXT,
         `attachments` INTEGER,
         `in_reply_to` TEXT,
         `in_reply_to_id` INTEGER,
         `references` TEXT
       )''')

