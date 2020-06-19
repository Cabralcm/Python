# Calculator function

# Using functions are arguments

def add(n1,n2):
    return n1 + n2

def substract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def calc(operation, n1,n2):
    return operation(n1,n2) #using the 'operation' argument as a function!

result = calc(multiply, 10,20)
print(result)
print(calc(add, 10, 20))

###

def calc(operation,n1,n2):
    return operation(n1,n2) #using the 'operation' argument as a function

#Arguments
result = calc(lambda n1,n2 : n1 * n2, 10, 20)
print(result)
print(calc(lambda n1,n2: n1+ n2, 10, 20))

###



