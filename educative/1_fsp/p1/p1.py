from typing import *

# Example Code
a = 4
b = 10.5

# print(type(a))
# print(type(b))

# print(a+b)
# print ((a+b) * 2)

# print (3/2)
# print(3 //2)
# print(3 % 2)
# print(3**2)

def MathOp(x,y):
    if y == 0:
        raise print("Must provide a non-zero value")
        return False
    float_div = x/y
    floor_div = x//y
    mod = x % y
    power = x ** y
    return [float_div, floor_div, mod, power]

output = MathOp()
for value in output:
    print(output)

#Check if number is even or odd
#Return 0 if number EVEN, 1 if number ODD.
def check_parity(n:int) --> int:
    result = 0
    while n:
        result ^= n & 1
        n >> 1
    return result

def check_parity_2(n:int)-> int:
    result = 0
    while n: #only runs if x is not zero!
        result ^= 1
        n = n & (n-1)   #bit-hack to return the least significant 1 bit
                        #drops the lowest set bit of n
    return result

def check_parity_3(n:int) -> int:
   return (n%2)

def inRange(x:int, y:int)-> bool:
    if x < 1/3 and y > 1/3:
        return True
    else:
        False

def inRange_2(x,y):
    return (x < 1/3 < y)
    
def getStr(string, count):
    out_string = ""
    for char in string:
        out_string += char*count
    return [out_string, len(out_string)]

def getStr2(s):
    s = s[:1] + s[0] + s[1:] #aabc
    s = s[:1] + s[0] + s[1:] #aaabc
    s = s[:3] + s[3] + s[3:] #aaabbc
    s = s[:3] + s[3] + s[3:] #aaabbbc
    s = s[:6] + s[6] + s[6:] #aaabbbcc
    s = s[:6] + s[6] + s[6:] #aaabbbccc
    return [s, len(s)]

#Find first occurance of b and ccc in the string
# input: aaabbbccc
def findOccurences(s):
    a = 0 #first occurance of b
    b = 0 #first occurance of ccc
    a = s.find("b")
    b = s.find("ccc")
    return [a,b]

def changeCase(s):
    return s.lower()

def changeCase(s):
    return [s.upper(), s.lower()]


