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

def findMax(input_list):
    currentMax = float("-inf")
    for val in input_list:
        currentMax = val if (val > currentMax) else currentMax
    return currentMax

print("Max")
input = [1,2,3]
print(findMax(input))

def findMaxIndex(input_list):
    current = float("-inf")
    for index, val in enumerate(input_list):
        if current > val:
            current = val
            cur_index = index


def findMaxIndex2(input_list):
    current = float("-inf")
    cur_index = 0
    for index in range(len(input_list)):
        if current < input_list[index]:
            current = input_list[index]
            cur_index = index
    return [current, cur_index]

def findMax3(l):
    maximum = l[0]
    for x in l:
        if x > maximum:
            maximum = x
    return maximum

def findMaxIndex3(l):
    max = l[0]
    o_index = index
    for index,x in enumerate(len):
        if x > max:
            max = x
            o_index = index
    return [max, o_index]

l = [1,2,3]
[ind, maxi] = findMaxIndex3(l)

def reverse(l):
    out_list = []
    for val in range(len(l),0,-1):
        out_list.append(l[val])
    print(out_list)
    return out_list

def reverse2(l):
    length = len(l)
    new_list = [None]*length
    for item in l:
        length = length -1
        new_list[length] = item
    return new_list

def reverse3(l):
    new_list = l[::-1]

# List splicing
#l[1:10:2]
#start 1st index, end 10th index, take steps of 2
# l[1:10:2] --> 
#First element is inclusive
#Second element is exclusive
#If step size exceeds the slice, 
# then take the first element referenced
'''
Ever since Python 1.4, the slicing syntax 
has supported an optional third ``step'' or
 ``stride'' argument. For example, these are
all legal Python syntax: L[1:10:2], L[:-1:1],
L[::-1]. This was added to Python at the 
request of the developers of Numerical Python,
which uses the third argument extensively. 
However, Python's built-in list, tuple, and 
string sequence types have never supported this
feature, raising a TypeError if you tried it.
Michael Hudson contributed a patch to fix
this shortcoming. 
'''
