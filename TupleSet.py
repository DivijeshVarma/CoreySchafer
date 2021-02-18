# Tuple
# we can't modify tuples 
# lists are mutable and tuples are immutable

tuple1 = ('c', 'c++', 'java', 'python')
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple1[0] = 'bash'
# tuple does not support item assignment
print(tuple1)
print(tuple2)

# sets

sets = {'c', 'c++', 'java', 'python', 'c'}
# unlike lists and tuples, sets don't care about order. and
# throws away duplicates.
# checks value is part of set
print(sets)
print('python' in sets)

# it really useful what value share or don't share with other sets.

set1 = {'c', 'c++', 'java', 'python'}
set2 = {'java', 'python', 'bash', 'ruby'}

# what courses in sets had common
print(set1.intersection(set2))
print(set1.intersection(set2))

# difference
print(set1.difference(set2))

# combine
print(set1.union(set2))


# Empty lists
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {}  # its a dictionary not set
empty_set = set()
