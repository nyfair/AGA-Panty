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

files = glob.glob('%s/*.unity3d' % sys.argv[1])
for f in files:
  mtime = os.path.getmtime(f)
  if mtime > ctime:
    fname = os.path.basename(f)
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
          shutil.copy(f, 'backup/%s' % fname)
        else:
          with open('tmp/%s' % fname, 'wb') as w:
            w.write(raw[32:])
with open('res.json', 'w') as fd:
  fd.write(json.dumps(res))

print('Use Unity Studio to open all unity3d files and export all assets under the "tmp" directory')
x = os.system('"Unity Studio\\UnityStudio.exe"')
if x == 0:
  files = glob.glob('tmp/**/*.png', recursive=True)
  for f in files:
    shutil.move(f, 'img/%s' % os.path.basename(f))
  shutil.rmtree('tmp')
