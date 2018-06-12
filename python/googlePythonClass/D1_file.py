import sys
import os



def Cat(filename):
  # read the file line by line, use less RAM than read in whole file
  f = open(filename, 'rU')
  for line in f:   
    # print line  # line string include new line at the end
    print line,   # ',' at the end, prohibits the new line at the end
  f.close()       # close file

def Cat2(filename):  
  # read the file as a list, need 20G RAM to store, if the file is 20G big
  f = open(filename, 'rU')
  lines = f.readlines()
  print lines
  f.close
  
def Cat3(filename):  
  try:
    f = open(filename, 'rU')
    text = f.read()
    print '--------', filename
    print text
    f.close
  except IOError: #print error if fails
    print 'IO Error', filename
  

# open a file for writing, this will zero out the file  
#to do
def print_line_to_file(filename, lines):
  f = open(filename, 'w')
  f.writelines(lines)
  f.close

def print_text_to_file(filename, text):
  f = open(filename, 'w')
  f.write(text)
  f.close

  
# find files in dir with ending
def files_in_dir (dir = './', ending= '.txt'):
  for file in os.listdir(dir):
    if file.endswith(ending):
      print file  


      
def main():
  args = sys.argv[1:]
  for arg in args:
    Cat3(arg)

if __name__ == '__main__':
  main()