import gzip
import json
from datetime import datetime

def log_database(conn, param, email):
  param = json.dumps(param)
  email_gz = gzip.compress(email.encode('ascii'))
  values = (param, email_gz)

  c = conn.cursor()
  c.execute('''
    INSERT INTO email_log (`param`, `email_gz`)
    VALUES (?, ?)
    ''', values)

def log_text(fname, param, email):
  from datetime import datetime

  with open(fname, 'a') as f:
    f.write("=== %s ===\n" % datetime.now())
    f.write("args: %s\n" % (" ".join(param),))
    f.write("-------------\n")
    f.write(email)
    f.write("\n\n")
    f.flush()

