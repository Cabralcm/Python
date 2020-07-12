# Dynamic Programming in Python

1) Basic Recursion
2) Top-Down
3) Bottom-up
    
> Recursion is the process of repeating a procedure. In CS, it refers to a function calling itself (directly or indirectly).

# Direct Recursion

```
def func(str, n):
    if n>0:             # This is the base case
        print(str, 'called func with n=', n)
        func('func', n-1) # Recursive Call

def main():
    func('main', 7)

main()
```

The order of the base case and recursive call are critical. 

For the output, the order of the `print` statement and the recursive call is very important. If the `print` statement comes before the recursive call, it is called **Tail Recursion**. This is because the recursive call is follwoing the processing `print` in this case. 

For the second case, when the `print` statement comes after the recursive call, it is called **Head Recursion** because the recursive call occurs at the start of the function before any other statement.

# Indirect Recursion

When two or more functions call themselves indirectly from eaceh other, we call it **indirect recursion**.

```
def func1(str, n):
  if n > 0:
    print (str, "called func1 with n =", n)
    func2("func1", n-1)

def func2(str, n):
  if n > 0:
    print (str, "called func2 with n =", n)
    func1("func2", n-2)

def main():
  func1("main", 7)
main()    
```

# Non-Linear Recursion

Both examples had a single call to themselves. This type of recursion is called *linear* recursion. 

**Multiple Recursion** is where a function calls itself multiple types,instead of once. 

Most of the recursion we tend to encounter is non-linear. For instance, the *Fibonacci series* algorithm. Which is a form of *binary recursion* (or two self-calls within a single function defintion).


