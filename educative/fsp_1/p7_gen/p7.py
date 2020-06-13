# Python Generators


def myrange(a,b):
    while a < b:
        yield a
        a += 1

a = myrange(2,4) # call the generator function which returns an object
# print(next(a)) # iterate through items using next!
# print(next(a))

# Example with For loop

def myrange(a, b):
    while a < b:
      yield a
      a += 1
# for value in myrange(1, 4):
#   print(value)

# Example with using next()

def myrange2(a, b):
    while a < b:
      yield a
      a += 1

seq = myrange(1,3)
# print(next(seq))
# print(next(seq)) 
# next(seq)  Will throw the StopIteration exception

# Example with for loops with generators

def squares(n):
    for value in range(n):
        yield value * value

sqr = squares(10)
# print(next(sqr))
# print(next(sqr))
# print(next(sqr))
# print(next(sqr))
# print(next(sqr))

# Generator to yield all the ODD numbers from 1 to n

def odd(n):
    for i in range(1,n+1):
        if i % 2 != 0:
            yield i
        else:
            continue

# official solution

def odd2(n):
    for i in range(n):
        if i % 2 is not 0:
            yield value

# Test
n = 10
# for val in odd(n):
#     print(val)

def reverse(n):
    for val in range(n,-1,-1):
        yield val

# Test
# for val in reverse(10):
    # print(val)

# Yield Fib Sequence from 1st to Nth Number

def fibonacci(n):
    out = []
    for i in range(n):
        if i == 0 or i == 1:
            out.append(i)
            yield i
        else:
            calc = out[i -1] + out[i - 2]
            out.append(calc)
            yield calc

# Test
for i in fibonacci(10):
    print(i)


