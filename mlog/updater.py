import email

def update_stage_0(conn):
  c = conn.cursor()
  c.execute('''
    SELECT id
    FROM email_log
    WHERE stage=0
    ''')

  ids = [row[0] for row in c]
  for lid in ids:
    values = (lid,)
    c.execute('''
      SELECT email
      FROM email_log
      WHERE id=?
      ''', values)

    content = c.fetchone()[0]

    m = email.message_from_string(str(content))
    subject = m.get('Subject')
    receiver = m.get('To')
    sender = m.get('From')
    date = m.get('Date')
    message_id = m.get('Message-ID')

    stage = 1
    values = (sender, receiver, subject, date, message_id, stage, lid)
    c.execute('''
      UPDATE email_log
      SET sender=?, receiver=?, subject=?, date_raw=?, message_id=?, stage=?
      WHERE id=?
      ''', values)

