#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

##NOTE: Jing: I'm supprise actul result linear_merge4 is fastest

# Additional basic list exercises
import timeit

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  new_list = []
  for num in nums:
    if num not in new_list:
      new_list.append(num)
  return new_list


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge1(list1, list2):
  # +++your code here+++
  merged_list = []
  
  # when both list is not empty
  while len(list1) and len(list2):
    if list1[0] <= list2[0]:
      merged_list.append(list1.pop(0))
    else:
      merged_list.append(list2.pop(0))

  # one or both list are empty, extend empty list will not change anything
  merged_list.extend(list1)
  merged_list.extend(list2)
  return merged_list

def linear_merge2(list1, list2):
  # +++your code here+++
  merged_list = []
  # smallest last
  list1.reverse()
  list2.reverse()
  
  # when both list is not empty
  while len(list1) and len(list2):
    if list1[-1] < list2[-1]:
      merged_list.append(list1.pop(-1))
    else:
      merged_list.append(list2.pop(-1))

  # one or both list are empty, extend empty list will not change anything
  list1.reverse()
  list2.reverse()
  merged_list.extend(list1)
  merged_list.extend(list2)
  return merged_list
  
def linear_merge3(list1, list2):
  # +++your code here+++
  merged_list = []    # largest first
  result      = []
  
  # when both list is not empty
  while len(list1) and len(list2):
    if list1[-1] > list2[-1]:
      merged_list.append(list1.pop(-1))
    else:
      merged_list.append(list2.pop(-1))

  # one or both list are empty, extend empty list will not change anything
  merged_list.reverse()
  result.extend(list1)
  result.extend(list2)
  result.extend(merged_list)

  return result
 
def linear_merge4(list1, list2):
  # +++your code here+++
  result = list1 + list2
  result = sorted(result)
  return result 

  
# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])
  repeat = 100000
  
  print
  print 'linear_merge1'
  start_time = timeit.default_timer()
  test(linear_merge1(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge1(['aa', 'zz'], ['bb', 'cc', 'xx']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge1(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  for n in range(repeat):
    linear_merge1(['aa', 'xx', 'zz'], ['bb', 'cc'])
  print(timeit.default_timer() - start_time)
  
  print
  print 'linear_merge2'
  start_time = timeit.default_timer()
  test(linear_merge2(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'zz'], ['bb', 'cc', 'xx']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  for n in range(repeat):
    linear_merge2(['aa', 'xx', 'zz'], ['bb', 'cc'])
  print(timeit.default_timer() - start_time)
  
  print
  print 'linear_merge3'
  start_time = timeit.default_timer()
  test(linear_merge3(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge3(['aa', 'zz'], ['bb', 'cc', 'xx']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge3(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  for n in range(repeat):
    linear_merge3(['aa', 'xx', 'zz'], ['bb', 'cc'])
  print(timeit.default_timer() - start_time)
  
  print
  print 'linear_merge4'
  start_time = timeit.default_timer()
  test(linear_merge4(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge4(['aa', 'zz'], ['bb', 'cc', 'xx']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge4(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  for n in range(repeat):
    linear_merge4(['aa', 'xx', 'zz'], ['bb', 'cc'])
  print(timeit.default_timer() - start_time)

if __name__ == '__main__':
  main()
    