#!/usr/bin/python
import os,sys,yaml
THUMB_SIZE = 150
BUCKET = 'maskify'
values = yaml.load(open('values.yml', 'r').read().replace('---\n', ''))
if len(sys.argv) < 2:
  print 'Usage: %s COMMAND' % sys.argv[0]
  sys.exit(0)
command = sys.argv[1].lower()
if command == 'thumbs':
  for mask in values['masks']:
    os.system('convert masks/%(i)s -resize %(sz)sx%(sz)s thumbs/%(i)s' % \
      {'i': mask['image'], 'sz': THUMB_SIZE})
elif command == 'publish':
  for mask in values['masks']:
    print 'Uploading %s' % mask['image']
    for folder in ('masks', 'thumbs'):
      os.system('cd %(f)s && aws put --public %(b)s/%(f)s/%(i)s %(i)s' % \
        {'i': mask['image'], 'f': folder, 'b': BUCKET})

