# regular expression, look from left to right, one find it and done
import re

match = re.search('iig', 'called piiig')
print match.group()         # 'iig'

def Find(pat, text):
  match = re.search(pat, text)
  if match: 
    print match.group()     # None, 0, counts as False
  else: print 'not find'

  
  
Find ('igs', 'called piiig')
Find ('x...g', 'called xii>g xi?ig')
Find ('\.com', 'called xii>g xi?ig.com')
Find (r'.com', 'called xcom xi?ig.com')         # the r meaning raw string
Find (r'\.com', 'called xcom xi?ig.com')
Find (r':\w\w\w', 'blah :c2a>t blash')          # \w word chars
Find (r':\d\d\d', 'blah3456 :123c2a>t blash')
Find (r'\d\s\d\s\d', '1 2 2')                   # \s whitespace char
Find (r'\d\s\d\s+\d', '1 2     2')              # + pultipe number
Find (r':\w+', 'bla bla :kitten blac blah')  
Find (r':\w+', 'bla bla :kitten123_& blac blah')    
Find (r':\S+', 'bla bla :kitten123_&  blac ')    #\S non-whitespace char
Find (r'\w[\w.]+@[\w.]+\w', 'bla .hello_.nich.p@gail.com.hk_. yass@yahoo.com') #[] some set of char

### this group thing does not work
## this does not work  
def FindGroup(pat, text):
  match = re.search(pat, text)
  if match: 
    print match.group(0)     # None, 0, counts as False
    print match.group(1)
  else: print 'not find'
  
FindGroup(r'([\w.]+)@([\w.]+)', 'bla hello.nich.p@gail.com.hk yass@yahoo.com')


def FindAll(pat, text):
  match = re.findall(pat, text)
  if match: 
    print 'find %d' % len(match), match
  else:
    print 'not find'
FindAll(r'[\w.]+@[\w.]+', 'bla .hello_.nich.p@gail.com.hk_. yass@yahoo.com')
FindAll(r'([\w.]+)@([\w.]+)', 'bla .hello_.nich.p@gail.com.hk_. yass@yahoo.com')