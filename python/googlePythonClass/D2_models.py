import os
import sys

# find file in current directory
filenames = os.listdir('./')
for filename in filenames:
  # this create relative path
  path = os.path.join(dir, filename)
  print 'file: %s, path: %s' % (file, path)
 
# dir exist
print check_dir('temp/foo')
print check_dir('temp/baz')

# create dir
os.mkdir('temp/baz')
print check_dir('temp/baz')
