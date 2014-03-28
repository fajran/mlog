import email

def parse(text):
  m = email.message_from_string(str(text))
  return m.get('Subject'), \
         m.get('To'), \
         m.get('From'), \
         m.get('Date'), \
         m.get('Message-ID')

