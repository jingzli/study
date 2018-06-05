# note for day1-2: list, sorting, tuples

# string handles similar to a list of chars
s = 'hello world'
print s[2:]	      # llo word, from 2 to the end, including 2
print s[:2]       # he, from 0 to 2, not including 2
print s.startswith('hello')    # True
print s.startswith('world')    # False


#list
####################################
a = [ 1, 2, 'aaa']
b = [3, 4]

print a + b			# [1, 2, 'aaa', 3, 4]

# a is pointing to the list, and b is pointing to the same list
# changing element in a will refect in b also
b = a 		

# make a copy, and a and c are two individule list
c = a[:]  

a = [1,2,3,4]

# print list
for num in a: print num

# check value in a list
print 2 in a		# true
print 14 in a 		# false

# append returns None and modify the list)
print a.append(5)	# None 
print a 			# [1, 2, 3, 4, 5]

# pop returns the a[0] and remove a[0] from the list
print a.pop(0)		# 1 
print a				# [2, 3, 4, 5]

# del modify the list a, remove element a[1], does not return anything
del a[1]			
print a				# [2, 4, 5]

#sort
########################################################
#help(sorted)		
# sorted(...)
#    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

# if sort see the list is numeric, it does numeric comparison
# sort reurn a sorted list, does not change the original list
a = [4,2,1,6]
print sorted(a)     			# [1, 2, 4, 6] 
print sorted(a,reverse=True)	# [6, 4, 2, 1]
print a							# [4, 2, 1, 6]

a = ['ccc','aaaaa','d', 'bb']
print sorted (a)				# ['aaaaa', 'bb', 'ccc', 'd']
#custon sorting, sort by lenth of elements, use len function
print sorted(a,key=len) 		# ['d', 'bb', 'ccc', 'aaaaa']

a[1] = 'aaaz'
print a							# ['ccc', 'aaaz', 'd', 'bb']

# define function for sorting
def Last(s): return s[-1]
print sorted(a, key=Last)		# ['bb', 'ccc', 'd', 'aaaz']		

b = ':'.join(a)				
print b							# 'ccc:aaaz:d:bb'
print b.split(':')				# ['ccc', 'aaaz', 'd', 'bb']

result = []
for s in a: result.append(s)
print result					# ['ccc', 'aaaz', 'd', 'bb']


# NOTE: do not modfy list when looping it, modify change a list structure
# generate list of numbers
print range(20)


# list length can change
# tuple length cannot change, tuple is like a string cannot be changed
a = (1,2,3)
a = [(1,'a'),(1,'b'),(2,'a')]
# tuple will be sorted by the first element and then sorted by the second element
print sorted(a)	# [(1, 'a'), (1, 'b'), (2, 'a')]

(x,y) = (1,2)
print x			# 1
print y			# 2
