import sqlite3
import sys
import json

from . import settings
from . import db
from . import log

def main():
  conn = sqlite3.connect(settings.DB_PATH)
  db.init(conn)

  param = sys.argv[1:]
  email = sys.stdin.read()
  log.log_database(conn, param, email)
  log.log_text(settings.LOG_PATH, param, email)

  conn.commit()

if __name__ == '__main__':
  main()

