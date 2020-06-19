# Sets

> A set is an unordered collection of data items.

A set is NOT indexed. Cannot access elements using indices or `get()`.

Mutable data structures (e.g. lists or dictionaries) cannot be added to a set. 
Adding a tuple is perfectly fine.

> A set is perfect when we need to keep track of the EXISTENCE of items

A set doesn't allow duplicates. 

We can convert another data structure to a set to remove any duplicates.

## Creating a set 

Sets are represented by curly braces: `{}`

```
my_set = {"educative", 1408, 3.14159, (True, False)}
```

Can also use the set constructor `set()`.

```
my_set = set()

another_set = set({'Educative", 1280, (True, False)})
```

## Adding (single, multiple)

To add a single item, we can use the `add()` method.

To add multiple items, we'd have to use `update()` method. The `input` for `update()` must be another `set, tuple, or string`.

```
my_set = set()

my_set.add(1)

my_set.update([2,3,4,5,6,7])
```

## Deleting elements

Using `discard()` or `remove()` operations can be used to delete a particular item from a set.

> The `remove()` method generates an error if the item is NOT found, unlike the `discard()` method. 

```
my_set = set({'Educative", 1280, (True, False)})

my_set.discard(1280)

my_set.remove( (True, False) )
```

## Iterating a Set 

The `for` loop can still be used with unordered data structures like sets. However, we wouldn't know the order in which the iterator moves through the elements, thus the elements will be picked randomly.

For instance

```
odd_list = [1,3,5,7]

unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

for num in unordered_set:
    if (not num % 2 == 0 ):
    # if num % 2 is not 0: #alternative condition
        odd_list.append(num)
```

# Built-in Functions

Instead of just using `in` keyword, can also use `find()` method. 

Returns the index at which a substring occurs within a string. If no instance of a substring is found, the method is `-1`.

`-1` is a conventional value that represents a `None` or failure in case the output was supposed to be positive.

For a string called `a_string`, `find()` can be used in the following way:

`a_string.find(substring, start, end)`











