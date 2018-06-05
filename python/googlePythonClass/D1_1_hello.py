#
# this class use python 2.4
# I'm using pythong 2.7

# import external modules
import sys

# define a main() function
def main():
   #print "Hello"
   #print sys.argv
   Hello(sys.argv[1])
   ## how to find out what is sys
   # dir(sys)  will show all functions
   # help(sys)  will give document
   # help(len)
 
def Hello(name):
   # number zero, empty string count as false, otherwise true.
   if name == 'Alice':
      name = name + '???'
   else:
      print 'Else'
   name = name + '!!'
   print 'Hello', name
   
# this is the standard boilerplate that calls the main function
if __name__ == '__main__':
   main()