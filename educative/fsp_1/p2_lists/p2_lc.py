# List Comprehension

l1 = [x*x for x in range(4)]
print(l1)

n= 10
l2 = [x*x for x in range(n) if (x%2 == 0)]
print(l2)

def getSquare():
    return [x**2 for x in range(1,11)]

print(getSquare())

def getCube():
    return [x**3 for x in range(1,21)]

def getCube2():
    return [x*x*x for x in range(1,21)]

def listOfEvenOdds():
    l1 = range(0,21)
    even = [x for x in l1 if x % 2 == 0]
    odd = [x for x in l1 if x % 2 != 0]
    return [even, odd]

def listOfEvenOdds2():
    l1 = [x for x in range(0,21) if (x %2 == 0 )]
    l2 =  [x for x in range(0,21) if (x %2 != 0 )]
    return [l1,l2]

def listOfEvenOdds3():
    l1 = [x for x in range(0,21) if (x % 2 == 0)]
    l2 = [x for x in range(0,21) if (x not in l1)]
    return [l1, l2]

def evenSquare():
    return [x**2 for x in range(0,21) if (x % 2 == 0)]

def evenSquare2():
    return [x*x for x in range(0,21,2)]

def getSquare2():
    return [x*x for x in range(0,21,2) if (x % 3 != 0)]
    
print(evenSquare())

def getSquare3():
    return [x**2 for x in range(0,21,2) if x%3 != 0]

def getSquare4():
    return [x**2 for x in range(0,21) if x%3 != 0 and x%2 == 0]


 




