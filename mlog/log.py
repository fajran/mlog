import json
from datetime import datetime

def log_database(conn, param, email):
  param = json.dumps(param)
  values = (param, email)

  c = conn.cursor()
  c.execute('''
    INSERT INTO email_log (`param`, `email`)
    VALUES (?, ?)
    ''', values)

def log_text(fname, param, email):
  from datetime import datetime

  f = open(fname, 'a')
  f.write("=== %s ===\n" % datetime.now())
  f.write("args: %s\n" % (" ".join(param),))
  f.write("-------------\n")
  f.write(email)
  f.write("\n\n")
  f.flush()
  f.close()

