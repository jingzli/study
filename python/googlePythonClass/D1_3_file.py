import sys

def Cat(filename):
  # read the file line by line, use less RAM than read in whole file
  f = open(filename, 'rU')
  for line in f:   
    # print line  # line string include new line at the end
    print line,   # ',' at the end, prohibits the new line at the end
  f.close()       # close file
  
  # read the file as a list, need 20G RAM to store, if the file is 20G big
  f = open(filename, 'rU')
  lines = f.readlines()
  print lines
  f.close
  
  
# python naming: XXXs --> list name
  
  
  
  
  
  
def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()