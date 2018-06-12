#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  img_urls_dict = {}
  hostname      = ''
  result        = []
  
  # Extract the hostname from the filename, any(\S+) non white space characters after '_' are hostname
  hostname_match = re.search(r'_(\S+)', filename)
  
  # return empty result if the input filename formate does not match expectatioin
  if not hostname_match:
    print 'RE Error', filename
    return result
  
  hostname = hostname_match.group(1)
  print 'hostname', hostname
  
  # read the file and search for image urls
  f = open(filename, 'rU')
  lines = f.readlines()
  for line in lines:
    match = re.search(r'GET (\S+jpg)', line)
    if not match: continue
    
    # find matched url that contains puzzle
    path = match.group(1)
    if 'puzzle' in path:
      img_url = "http://" + hostname + path
      
      # if img_url not in result:
        # result.append(img_url)
        
      # this will only create new item if the img_url does not exist in dict
      img_urls_dict[img_url] = 1
  
  # result = sorted(result)
  result = sorted(img_urls_dict.keys())
  # print '\n'.join(result)
  return result
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  image_index = 0
  images      = []
  index_file_path = os.path.join(dest_dir, 'index.html')
  

  
  # check if the dest_dir exist, make new directory if does not exist. 
  if not os.path.isdir(dest_dir): 
    print 'The dest_dir does not exist, make new dir: %s' % dest_dir
    os.mkdir(dest_dir)

  # download img_url
  for img_url in img_urls:
    local_name = 'img%d.jpg' % image_index 
    image_local_path = os.path.join(dest_dir, local_name)
    print 'GET %s and save to %s' % (img_url, image_local_path)
    urllib.urlretrieve(img_url, image_local_path)
    images.append(local_name)
    image_index += 1
    
  
  # write to index.html file
  index_f = open(index_file_path, 'w')
  index_f.write('<html><body>\n')
  for image in images:
    index_f.write('<img src="%s">' % (image))
  
  index_f.write('\n</body></html>\n')
  index_f.close()


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
