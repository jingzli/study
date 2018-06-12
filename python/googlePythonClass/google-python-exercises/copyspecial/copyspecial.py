#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def copy_to(todir, file_paths):
  """ 
      copy files in file_paths to the todir
      create directory if todir does not exists
  """
  # print 'start copy_to fuction\ndir: %s\nFiles:\n%s' %(todir, '\n'.join(file_paths))
  if not os.path.isdir(todir): 
    print 'The todir does not exist, make new dir: %s' % todir
    os.mkdir(todir)
  for file_path in file_paths:
    (file_dir, file_name) = os.path.split(file_path)
    dest_file_path = os.path.join(todir, file_name)
    print 'copy %s, to %s' %(file_path, dest_file_path)
    shutil.copy(file_path, dest_file_path)
  
  
def zip_to(tozip, file_paths):
  # have to end with 7z
  """ 
      zip files in file_paths to tozip file, 
      if tozip file does not end with .zip, add .zip to the end
      
      command line: set PATH=%PATH%;C:\Program Files\7-Zip\
      7z a file.zip file  (a: add file to achieve)
  """
  if not tozip.endswith('.zip'):
    tozip += '.zip'
  
  # delet zip file if exists
  if os.path.exists(tozip):
    print 'zip file exists, delet the file: %s' % tozip
    os.remove(tozip)
  
  # add file in zip from command line
  for file_path in file_paths:
    cmd = "7z a %s %s" % (tozip, file_path)
    print 'run cmd: %s' %cmd
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    (output, error) = process.communicate()
    if error:
      print 'ERROR: %s %s' % (error, output)
  return 1

# get file path for all the files in the dir 
def get_file_paths(dir):
  """ get file path for all files in dir
      check input dir is directory, print error if it is not a directory
  """
  file_paths = []
  if os.path.exists(dir): 
    filenames = os.listdir(dir)
    for filename in filenames:
      path = os.path.join(dir, filename)
      # file_paths.append(os.path.abspath(path)) 
      file_paths.append(path)
  else:
    print 'ERROR, path does not exists:', dir
  return file_paths

# get special file path in the dir 
def get_special_file_paths(dir):
  file_paths = []
  if os.path.isdir(dir): 
    filenames = os.listdir(dir)
    for filename in filenames:
      match = re.search(r'__(\w+)__', filename)
      if match:
        path = os.path.join(dir, filename)
        # file_paths.append(os.path.abspath(path)) 
        file_paths.append(path)
  else:
    print 'ERROR, dir does not exists:', dir
  return file_paths  
    
def exit_with_usage(args):
  print "user input argument: %s" % ' '.join(args)
  print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
  sys.exit(1)
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    if len(args) < 3:
      exit_with_usage(args)
    else:
      del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    if len(args) < 3:
      exit_with_usage(args)
    else:
      del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  file_paths = []
  for arg in args:
    # file_paths.extend(get_file_paths(arg))
    file_paths.extend(get_special_file_paths(arg))
  if todir:
    copy_to(todir, file_paths)
  if tozip:
    zip_to(tozip, file_paths)
  else:
    print 'files pathes ----------------'
    print '\n'.join(file_paths)
  
if __name__ == "__main__":
  main()
