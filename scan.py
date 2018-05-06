import glob
import json
import os
import re
import shutil
import sys

pattern = re.compile(b'chr([123])_(\d{3})_(\d{2})')
types = {b'1':'model', b'2':'costume', b'3':'chara'}

def md(x):
  if not os.path.exists(x):
    os.mkdir(x)

md('img')
md('backup')
md('tmp')
res = {'time': 0}
ctime = 0
if os.path.exists('res.json'):
  with open('res.json', 'r') as fd:
    res = json.loads(fd.read())
    ctime = res['time']

files = glob.glob('jp.colopl.alice/files/*.unity3d')
for f in files:
  fname = os.path.basename(f)
  f1 = 'backup/%s' % fname
  f2 = 'mod/%s' % fname
  s1 = os.path.getsize(f1) if os.path.exists(f1) else 0
  s2 = os.path.getsize(f2) if os.path.exists(f2) else 0
  if os.path.getsize(f) in [s1, s2]:
    continue
  mtime = os.path.getmtime(f)
  if mtime > ctime:
    if mtime > res['time']:
      res['time'] = mtime
    with open(f, 'rb') as fd:
      raw = fd.read()
      x = pattern.search(raw)
      if not x is None:
        x = x.groups()
        key = '%s_%s' % (x[1].decode(), x[2].decode())
        print('%s %s %s' % (fname, key, types[x[0]]))
        if x[0] == b'1':
          res[key] = fname[:32]
          shutil.copy2(f, 'backup/%s' % fname)
        with open('tmp/%s' % fname, 'wb') as w:
          w.write(raw[32:])
with open('res.json', 'w') as fd:
  fd.write(json.dumps(res))

print('Use Unity Studio to open all unity3d files and export all assets under the "tmp" directory with "cha" filter')
x = os.system('"Unity Studio/UnityStudio.exe"')
if x == 0:
  files = glob.glob('tmp/**/*.png', recursive=True)
  for f in files:
    shutil.move(f, 'img/%s' % os.path.basename(f))
  shutil.rmtree('tmp')
