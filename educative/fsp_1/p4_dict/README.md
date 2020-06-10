# Dictionaries

Data structures with index values by a given key (key-value pairs).
Dictionaries are composed of, keys and values.

Key is the reference that can be easily referenced from the dictionary in O(1) time. Thus dictionaries in Python are built upon the more general data structure called a Hash Table. Hash tables have indexes that are generated mathematically using a hash function, which take the dictionary key as an input. This all occurs "under the hood", and does not need to be configured by an individual using dictionaries in Python.

General syntax:

```
DictionaryName{
    key1: value1,
    key2: value2,
    key3: value3,
    .
    .
    .
    keyN: valueN
}
```

Each key in a dictionary must be **unique** (like a primary key in a database), thus allowing us to know which value to return for a given key.

Dictionaries are NOT sorted. 

We assign a key (int, float, string) to each value, instead of a numerical index for a list (which is a dynamically resizing Array).

### Ordinary Dictionary

> The order in which keys are inserted are NOT maintained when the elements are printed (or extracted from the dictionary). This changes every time the code is run!


### Ordered Dictionary
Can create an **ordered dictionary** which preserves the order in which the keys are inserted.

Import the `OrderedDictionary` from the `collections` library.

Call the `OrderedDictionary()` built-in method.


### Accessing Items from Dictionary

Dictionary items can be  *immutable* objects. They don't need to be strings!

```
d = {
    0: [0, 0, 0],
    1: [1, 1, 1],
    2: [2, 2, 2],
}

print d[2]
```

Looping to get all **KEYS** from a Dictionary

> Recall, the dictionary isn't necessarily printed in the order it was saved!

```
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

for x in ages:
  print(x)
```

Looping to get all **VALUES** from a Dictionary

```
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

for x in ages:
  print(ages[x])
```

Safer way of extracting values from a dictionary:

```
 if 'z' in dict: print dict['z']     ## Avoid KeyError
  print dict.get('z')  ## None (instead of KeyError)
```

A dictionary can be made within a dictionary. And you can use other dictionaries as values.

Akin to a pointer to pointers.

# Indexing Speeds in Python

https://stackoverflow.com/questions/35640780/python-fastest-way-to-find-indexes-of-item-in-list


# Sorting lists in Python

```
sort() -- Works on the same list
my_list.sort(key = . reverse= )

sorted() -- Returns a new list that is sorted
sorted(list = my_list, key= , reverse = )
```

