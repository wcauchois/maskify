#!/usr/bin/python
import os,sys,yaml
THUMB_SIZE = 150
BUCKET = 'maskify'
values = yaml.load(open('values.yml', 'r').read().replace('---\n', ''))
if len(sys.argv) < 2:
  print 'Usage: %s {thumbs,publish}' % sys.argv[0]
  print '  Reads data from values.yml'
  sys.exit(0)
command = sys.argv[1].lower()
if command == 'thumbs':
  try:
    os.mkdir('thumbs')
  except OSError:
    pass
  for mask in values['masks']:
    os.system('convert masks/%(i)s -resize %(sz)sx%(sz)s thumbs/%(i)s' % \
      {'i': mask['image'], 'sz': THUMB_SIZE})
elif command == 'publish':
  for mask in values['masks']:
    print 'Uploading %s' % mask['image']
    for folder in ('masks', 'thumbs'):
      os.system('cd %(f)s && aws put --public %(b)s/%(f)s/%(i)s %(i)s' % \
        {'i': mask['image'], 'f': folder, 'b': BUCKET})

