# Orderd Dict

# This dictionary keeps track of the order of keys AS THEY ARE ADDED!!

# If you create a regular dict, you will note that it is an unordered data collection.

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)
#{'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

# Typically, with a hash table or dictionary, the order in which the key/value pairs are printed are random

# If you need the keys sorted, you may have to implement

keys= d.keys()
print(keys)

keys = sorted(keys)
print(keys)

for key in keys:
    print(key, d[key])

from collections import OrderedDict

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
#OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

print("Ordered Dict")
for key in new_d:
    print(key, new_d[key])

print("Also ordered Dict")
for key,value in new_d.items():
    print(key,value)

# The values in the ordered dictionary will retain their order!!

# when you add new keys to the ordered dict, they will be added to the end of the dictionary, instead of being automatically sorted.

# When you compare two ordered Dicts, they will not only test the items for equality, but also that their order is correct.

# A regular dictionary only looks at the contents of the dictionary (if a key exists), but doesn't care about it's order!

# Additional methods: 
# popitem
# move_to_end

# popitem - return and remove a (key,item) pair.
# move_to_end method will move an existing key to either end of the OrderedDict.
# The item will be moved right end if the last argument for OrderedDict is set to True (which is the default), or to the beginning if it is False

# lastly, ordereddicts support reverse iteration using Python's reverse built-in function!

print("reversed order!")
for key in reversed(new_d):
    print(key,new_d[key])


