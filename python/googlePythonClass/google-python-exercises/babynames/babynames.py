#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# https://www.ssa.gov/oact/babynames/
import sys
import re
import os


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""  
debug_flag = 0

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  print 'start extract_names', filename
  
  # open file as read only, and read file 
  f = open(filename, 'r')   
  lines = f.readlines()
  f.close
  
  # parse each line
  output_list     = []
  name_rank_dic   = {}     # each item contains: (name, rank)
  year            = 0
  
  for line in lines:
    ### find year
    if year == 0:
      match = re.search('Popularity in (\d+)', line)
      debug_print (line)
      if match:
        year = match.group(1)
        debug_print( 'year: %s' % year)
    
    ### find baby name and ranking
    else:
      match = re.search(r'\<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
      debug_print (line)
      if match:
        popularity  = match.group(1)
        boy_name    = match.group(2)
        girl_name   = match.group(3)
        debug_print ( "Popularity: %s,  Boy Name: %s,  Girl Name: %s" % (popularity,boy_name,girl_name))
        
        ### store name in name_rank_dic, 
        # choose more popular rank for the same name (something boy girl has same name)
        for name in [boy_name, girl_name]:
          if name in name_rank_dic:
            if popularity < name_rank_dic[name]:
              name_rank_dic[name] = popularity
          else:
            name_rank_dic[name] = popularity
      else:
        debug_print ('not match')
      
  ### sort name_rank_list and print to file
  output_list.append(year)
  for name in sorted(name_rank_dic.keys()): 
    debug_print ('Name Rank: %s %s' % (name, name_rank_dic[name]))
    output_list.append('%s %s' % (name, name_rank_dic[name]))

  return output_list

def extract_names_2(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  print 'start extract_names', filename
  output_list     = []

  # read whole text and process
  f = open(filename, 'r')   
  text = f.read()
  f.close

  # Get the year
  year_match = re.search('Popularity in (\d+)', text)
  if not year_match:
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = year_match.group(1)
  output_list.append(year)
  
  # find baby name and ranking
  # store name in name_rank_dic, 
  # choose more popular rank for the same name (something boy girl has same name)
  matches = re.findall(r'\<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  name_rank_dic   = {}     # each item contains: (name, rank)
  for match in matches:
    (rank,boy_name,girl_name)  = match
    for name in [boy_name, girl_name]:
      if name in name_rank_dic:
        if rank < name_rank_dic[name]:
          name_rank_dic[name] = rank
      else:
        name_rank_dic[name] = rank
      
  ### sort name_rank_list and print to file
  for name in sorted(name_rank_dic.keys()): 
    debug_print ('Name Rank: %s %s' % (name, name_rank_dic[name]))
    output_list.append('%s %s' % (name, name_rank_dic[name]))

  return output_list

def debug_print (debug_string):
  if debug_flag == 1:
    print debug_string
    

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile]  file [file ...]'
    print 'usage: [--summaryfile]  --all'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file    
  ## process all filenames ending with html in the folder
  if not args:
    print 'usage: [--summaryfile]  file [file ...]'
    print 'usage: [--summaryfile]  --all'
    sys.exit(1)
    
  if args[0] == '--all':
    del args[0]
    for filename in os.listdir('./'):
      if filename.endswith('.html'):
        args.append(filename)
  
  # process files
  for filename in args:
    output_list = [] 
    if os.path.isfile(filename) and filename.endswith('.html'):
      output_list = extract_names_2(filename)
      # print to file or screen
      text = '\n'.join(output_list)
      if summary:
          outf_name = filename + '.summary'
          outf = open(outf_name, 'w')
          outf.write(text + '\n')
          outf.close()
          print outf_name, 'created'
      else:
        print text
    else:
      print 'ERROR:', filename, ' does not exsts or not end with .html!!!'
  
   
    
if __name__ == '__main__':
  
  main()
