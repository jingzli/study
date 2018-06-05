# hash table, also called dictionary, is buildin in python 
# * always talk to it in terms of key
# * HashTables is very fast at key retrieval. 


### define hash
d = {}
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gamma'
print d ['a']         # alpha
print d.get('x')      # None, not find in hash

print 'a' in d        # True
print 'x' in d        # False

print d.keys()        # ['a', 'g', 'o'], in ramdom order
print d.values()      # ['alpha', 'gamma', 'omega'], in ramdon order as same as key's order

#### print Hash
for k in sorted(d.keys()): print 'key:', k, '->', d[k]
# key: a -> alpha
# key: g -> gamma
# key: o -> omega

print d.items()       
# [('a', 'alpha'), ('g', 'gamma'), ('o', 'omega')], print list of tuples, each tuple is length 2 and represents one binding in hash 
for tuple in d.items(): print tuple


