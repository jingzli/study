#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def read_words_infile(filename):
  words_counts = {}                 # hash: key(word), value(word_count)
  f = open(filename, 'rU')          # 'rU': open file with universial new line
  for line in f:
    words = line.split()
    # print line,                   # print ignore ending newline     
    # print words
    
    for word in words:
      word = remove_special_char(word)
      word = word.lower()           # convet word to lower case
      if len(word) > 0:             # do nothing for empty string        
        if word in words_counts:    # if word exists in words_counts, increase count
          words_counts[word] += 1 
        else:                       # else define new word with count 1
          words_counts[word] = 1 
    # print words_counts
  f.close
  return words_counts
  
def remove_special_char(word):
  clean_word    = ''
  special_chars = ['\"', '\'', '-','(', ')', ',', '.', ';', '!', '?', ':', '`']
  deapth        = 4   # looks into first and last 4 chars for special_chars
  
  clean_word = word
  while deapth >0 and len(clean_word):
    deapth -= 1
    # only remove leading and ending special_chars
    if clean_word[0] in special_chars:
      clean_word = clean_word [1:]
    
    if clean_word[-1] in special_chars:
      clean_word = clean_word [:-1]
    
  # print word, clean_word 
  return clean_word


def print_words(filename):  
  words_counts = read_words_infile(filename)
  # print words_counts.items()
  # print words_counts
  
  # print as sorted key(words)
  for key in sorted(words_counts.keys()):
    print '%s %d' % (key, words_counts[key])
  print len(words_counts)
  
  return


def sort_fuc(input):
  # sort by last element of the tuple
  return input[-1]
  
def print_top(filename):
  print_num = 20
  words_counts = read_words_infile(filename)
  tuples = words_counts.items()
  for tuple in sorted(tuples, key = sort_fuc, reverse = True):
    print '%s %d' % (tuple[0], tuple[1])
    print_num -= 1
    if print_num < 1:
      break
  return


####
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
