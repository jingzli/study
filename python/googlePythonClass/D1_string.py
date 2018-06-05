#build in Strinng methods
a = 'Hello'

# run a method on a object
print a
# Hello

print a.lower()
# hello

print a.find('e')
# 1

print a[1]
# e
print len(a)
# 5

# index of the string
print a[1:3]   # from 1 but not include 3
# el

print a[1:]    # from 1 to end
# ello

print a[-1]    # line -1, refer to right hand side
# o

print a[:-3]
# He
print 'Hi %s I have %d donuts' % ('Alice',12)
# Hi Alice I have 12 donuts