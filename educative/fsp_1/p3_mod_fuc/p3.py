# Modules and Functions in Python

import math

def findGCD(a,b):
    less = a if (a < b) else b
    for val in range(less,1,-1):
        if (a % val == 0) and (b % val == 0):
            return val
    return 1

def findGCD2(a,b):
    return math.gcd(a,b)

print(findGCD(10, 20))

def calcSinCosTan(x):
    return [math.sin(x), math.cos(x), math.tan(x)]

def findMax(a,b):
    return a if a < b else b

def findMax2(a,b):
    return max(a,b)

def isDivisible(x,y):
    if x == 0:
        return False
    if x % y == 0:
        return True
    else:
        return False

# Recursion
# Base Conditoin
# Recursive function (call)

def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n * factorial(n-1)

def fact2(n):
    if (n<=1):
        return 1
    n=1
    for val in range(1,n+1):
        n *= val
    return n


cache = {}

def fib_bf(n):
    if (n<=1):
        return 1
    return fib_bf(n-1) + fib_bf(n-2)

def fib2(n):
    if (n <= 1):
        return 1
    if n not in cache:
        cache[n] = fac(n-1) + fac(n-2)
    return cache[n]

def fib(n):
    if (n <= 1):
        return 1
    f_1, f_2 = 1,0
    for val in range(1,n+1):
        f = f_1 + f_2
        f_1, f_2 = f, f_1
    return f_1

print("Factorial")
print(fib(5))

def sum_N_Numbers(n):
    sum = 0
    for val in range(1,n+1):
        sum += val
    return sum

def sum_N_Numbers2(n):
    return sum(range(1,n+1))

def sum_N_Numbers3(n):
    if n <= 1:
        return 1
    return n + sum_N_Numbers3(n-1)

for value in [0,1,2,3,4,5]:
    print(value * value)

def sumList(in_list):
    x= 0
    return [sum+sum for sum in in_list]

print(sumList([1,2,3]))