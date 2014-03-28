import sqlite3
import sys
import json

from . import settings
from . import db
from . import updater

def main():
  conn = sqlite3.connect(settings.DB_PATH)
  db.init(conn)

  updater.update_stage_0(conn)

  conn.commit()

if __name__ == '__main__':
  main()

