# Python Recursion 

def rec_count(num):
    print(num)
    if num <= 0: # Base case
        return 0
    rec_count(num - 1) # Recursive all with a decremented argument
    print(num)

rec_count(5)