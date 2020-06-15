# Python Generators

Generators and Yield

As seen before, iterators are objects that are regularly used with `for loops`. 
In order words, iterates are objects that implement the **iteration protocol**. 

A Python generator is a convenient way to implement an iterator.

Instead of a class, a generator is a function which returns a value each time the `yield` keyword is used. 

As an example:

```
def myrange(a,b):
    while a < b:
        yield a
        a += 1

a = myrange(2,4) # call the genreator function which returns an object 
print(next(a)) # iterate through items using next
print(next(a))
```

Akin to iterators, generators can be used with the `for loop`

```
def myrange(a,b):
    while a < b:
        yield a
        a += 1

for value in myrange(a,b):
    print (value)
```

Under the hood, generators behave similarly to iterators. 

The interesting thing about **generators** is the `yield` keyword. 
The `yield` keyword works much like the `return` keyword, however unlike `return`, it allows the function to eventually RESUME its execution!

In order words, each time the next value of a generator is needed, Python wakes up the function and resumes its execution from the `yield` line as if the function had never executed!

Generator functions can use other functions inside. For instance, it is very common to use the `range` function to iterate over a sequence of numbers.

```
def squares(n):
    for value in range(n):
        yield value * value

sqr = squares(10):
print(next(sqr))
print(next(sqr))
print(next(sqr))
```
