# Python Iterators

# Problem - Return all the positive even numbers from 1 to (n). 

class MyRange:

    def __init__(self, n):
        self.curr = 1
        self.n = n
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < self.n:
            
            value = self.curr
            self.curr += 1
            return value
        else:
            raise StopIteration

# Test Case
n= 10
myrange = MyRange(n) #Where n is an integer
print(next(myrange))

## Solution

class MyRange:

    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self

    def next(self):
        evenArray = [] # next method returns this list
        for num in range(1, self.n+1):
            if num % 2 == 0: #checks if the number if even
                value = num
                evenArray.append(num) # add the event number to the list
            else: # number was odd
                num += 1
                # pass
        return evenArray

# Test Cases
n = 12
myrange = MyRange(n)
print(myrange.next())

class SuperRange:

    def __init__(self,n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def next(self):
        outArray = [None]*(self.n+1)
        i = 0
        while self.n >= 0:
            outArray[i] = self.n
            i += 1
            self.n -= 1
        return outArray

# Test
n = 10
myrange = SuperRange(n)
print(myrange.next())

## Formal Solution

class MySuperRange:

    def __init__(self,n):
        self.n = next
    def __iter__(self):
        return self
    def next(self):
        outArray = []
        for i in range (n,-1,-1):
            outArray.append(i)
        return outArray

n = 10
myrange = MySuperRange(n)
print(myrange.next())

# Problem - Fibonacci Sequence
# Output - range of Fibonacci numbers from 0 to n

class Fib:

    def __init__(self,n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def next(self):
        if n == 0:
            return [0]
        if n== 1:
            return [0,1]

        outArray = [None]*(self.n)        
        f_1, f_2 = 1,0
        outArray[:2] = [0,1]
        for i in range(2,self.n):
            f = f_1 + f_2
            outArray[i] = f
            f_1, f_2 = f, f_1
        return outArray

fib = Fib(10)
print(fib.next())
            
## Formal Solution

class MyRange:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        outArray = []
        for i in range(self.n): # from n to 0
            if i == 0 or i == 1:
                myArray.append(i)
            else:
                myArray.append( myArray[i-1] + myArray[i-2])
        return myArray

# Test
myrange = MyRange(10)
print(myrange.next())

