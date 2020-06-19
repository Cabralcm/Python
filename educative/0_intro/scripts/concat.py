# Input int(), output str()

def rep_cat(x,y):
    return str(x)*10 + str(y)*5

# Iterative
def fact(n):
    if n <= 1:
        return 1
    output = 1
    for x in range(1,n+1):
        output *= x
    return output

print(fact(5))

# Recursive 
def fact2(n):
    if n <= 1: #Base case
        return 1
    return n * fact2(n-1) #Recursive Call

print(fact2(5))