import base64
import email
import os

from . import settings

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
    attachments = _count_attachments(m)

    stage = 1
    values = (sender, receiver, subject, date, message_id, stage,
              attachments, lid)
    c.execute('''
      UPDATE email_log
      SET sender=?, receiver=?, subject=?, date_raw=?, message_id=?, stage=?,
          attachments=?
      WHERE id=?
      ''', values)

    path = settings.ATTACHMENT_SAVE_PATH
    _save_attachments(lid, m, path)

def _count_attachments(m):
  return sum(map(_is_attachment, m.walk()))

def _is_attachment(m):
    cd = m.get('Content-Disposition')
    return cd is not None and cd.startswith('attachment')

def _save_attachments(lid, m, path):
  index = 0
  for item in m.walk():
    if not _is_attachment(item):
      continue

    fname = item.get_filename()
    mtype = item.get_content_type()
    payload = item.get_payload()
    content = base64.decodestring(payload)

    _, ext = os.path.splitext(fname)
    target = os.path.join(path, '%s-%s%s' % (lid, index, ext))

    f = open(target, 'wb')
    f.write(content)
    f.close()

    index += 1

