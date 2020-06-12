# Python Iterators

Previously seen in Python, using "for" or "while" loops to iterate over the contents of objects:

```
for value in [0,1,2,3]:
    print(value)
```

Objects that can be used with a for loop --> Iterators

An iterator is an object that follows the *iteration protocol*

The built-in `iter` method can be used to build iterator objects.

The `next` method can be used to gradually (incrementally) iterate over their content:

```
my_iter= ([0,1,2,3])
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
```

If there are no more elements (reach the end of the iterator), the iterator raises a `StopIteration` Exception!

# Iterator Classes

Iterators can be implemented as classes; you just need to implement the `__next__` and `__iter__` methods!

Here is an example of a class that mimics the `range` function, returning all values from `a` to `b`:

```
class MyRange:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __iter__(self): #returns the Iterator Object itself 
        return self
    
    def __next__(self): #returns the next item in the sequence
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration
```

Basically, on every call to `next`, it moves forward the internal variable `a` and returns its value. When it reaches 'b', it raises the `StopIteration` exception. You can observe this behavior by uncommenting the last line.

```
myrange = MyRange(1,4):
print(myrange.next())
print(myrange.next())
print(myrange.next())
```

This returns:

```
1
2
3
```

Best of all, we can use this iterator within a `for loop`!

```
*SAME CLASS AS BEFORE*

class MyRange:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __iter__(self):
        self
    
    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration
        
for value in MyRange(1,4):
    print(value)
```


