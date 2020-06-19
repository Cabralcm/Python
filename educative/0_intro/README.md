# Python

High-level language

Interpreted

High-Level syntax --> Byte code --> machine code

Compared to C++, code is compiled into executable, and then can be executed.

Python compiles the code behind the scenes, we can directly run the code.

Python uses
1) Web Apps
2) Data Science
3) AI
4) Image Processing
5) Operating Systems

Data Type - defines the type and range of values that item can have.

Three main data types
1) Numbers
2) Strings
3) Booleans

Variable - a name to which a value can be *assigned*

Variables are **mutable**

# Naming Convention

`snake_case` vs `camelCase`

# Numbers

Python Numbers --> {Integers, Floating-Point Numbers, Complex Numbers}

Memory for an integer depends on its value. E.g. 0 will take up 24 bytes, and 1 takes up 28 bytes.

# Floating-Point Numbers

Decimal numbers

A float occupies 24 bytes of memory.

# Complex Numbers

`complex()` is used to create complex numbers.

complex(real, imaginary)

`print(complex(10,20))`

**Output**
(10+20j)

> In normal mathematics, the imaginary part of a complex number is denoted by `i`. However, Python follows the *electrical engineering* convention which uses `j`.

A complex number usually takes up 32 bytes of memory.

Complex numbers are useful for modelling physics and electrical engineering models.

# Booleans

`True` or `False`.

# Strings

> A collection of characters closed within single or double quotation marks.

Strings can be empty or filled with white space.

Length --> `len()`

Indexing --> akin to a list (0, n-1)

Access --> obtain letters via index, `my_string[1]`

Reverse Indexing --> negative numbers (starting with -1)

## Slicing

slicing --> my_string[start:stop]

slice with step --> my_string[start:end:step]

Reverse slicing --> my_string[start:end:neg_step]

## Partial Slicing

if `start` not provided, substring will have all characters until the `end` index.

If `end` not provided, substring will begin from `start` and go all the way to the end.

# Operators

(Operand) [Operator] (Operand) --> Output

**in-fix operators** - appear between two operands, usually known as *binary* operators (two operands).

**prefix operators** - works on one operand, appears before it. 
Prefix operators are known as **unary** operators.

## Operators Types
1) Arithmetic operators
2) Comparison operators
3) Assignment operators
4) Logical operators
5) Bitwise operators

| Operator | Purpose | Notation|
|---|---|---|
| `()` | Parentheses | Encapsulates the Precedent Operator|
| `**` | Exponent | In-fix | 
| `%, *, /, //` | Modulo, Multiplication, Division, Floor Division | In-Fix |
| `+, -` | Addition, Subtraction | In-Fix |

## Comparison operators

| Operator | Purpose | Notation|
|---|---|---|
| `> `	    | Greater Than 	               | In-fix
| `< `	    | Less Than 	               | In-fix
| `>=`  	| Greater Than or Equal To 	   | In-fix
| `<=`  	| Less Than or Equal To 	   | In-fix
| `==`  	| Equal to 	                   | In-fix
| `is`  	| Equal to 	                   | In-fix
| `is not` 	| Not Equal To 	               | In-fix

> Result of a comparison is always a `bool`

If comparison is correct --> `True`
Otherwise, value is `False`

# Assignment

| Operator | Purpose | Notation|
|---|---|---|
| = 	        | Assign 	                   | In-fix
| += 	        | Add and Assign 	           | In-fix
| -= 	        | Subtract and Assign 	       | In-fix
| *= 	        | Multiply and Assign 	       | In-fix
| /= 	        | Divide and Assign 	       | In-fix
| //= 	        | Divide, Floor, and Assign 	|In-fix
| **= 	        | Raise power and Assign 	   | In-fix
| %= 	        | Take Modulo and Assign 	   | In-fix
| \|=, &=, ^= 	| OR/AND/XOR and Assign 	   | In-fix
| >>= 	        | Right-shift and Assign 	   | In-fix
| <<= 	        | Left-shift and Assign 	   | In-fix

# Logical Operators

| Operator | Purpose | Notation|
|---|---|---|
| and| 	AND| 	In-fix
| or |	OR 	|In-fix
| not| 	NOT| 	Prefix

## Bit Value

Binary - 1's and 0's

Boolean equivalence --> True == 1, False == 0 

```
print(10 * True)
print(10 * False)
```
**Output**
10
0

# Bitwise Operators

| Operator | Purpose | Notation|
|---|---|---|   
| & 	| Bitwise AND 	    | In-fix
| \| 	| Bitwise OR 	    | In-fix
| ^ 	| Bitwise XOR 	    | In-fix
| ~ 	| Bitwise NOT 	    | Prefix
| << | 	Shift Bits Left 	| In-fix
| >> | 	Shift Bits Right 	| In-fix

> AND can be thought of as multiplication between two operands.

```
num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)  # 00000
print(num1 | num2)  # 11110
print(num1 ^ num2)  # 11110
print(~num1)  # 1111 0101
print(num1 << 3)  # 0101 0000
print(num2 >> 3)  # 0010
```

> In simple terms, AND can be thought of as multiplication between two operands.

# String Operations

```
print('a' < 'b') # 'a' has a smaller Unicode value

house = "Gryffinder"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"

print(house == new_house)

print(new_house <= house)

print(new_house >= house)

**Output**
True
True
False
False
True
```

## Concatenation

first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name)

The `*` operator, allows us to multiply a string, resulting in a repeating pattern:

```
print("ha" * 3)
```

## Search 

```
random_string = "This is a random string"

print('of' in random_string) # Check whether 'of' exists in a random_string

print('random' in random_string) # 'random' exists!
```

# Conditionals

> A conditional statement is a Boolean expression that, if `True`, executes a piece of code.


# Built-in Functions

Instead of just using `in` keyword, can also use `find()` method. 

Returns the index at which a substring occurs within a string. If no instance of a substring is found, the method is `-1`.

`-1` is a conventional value that represents a `None` or failure in case the output was supposed to be positive.

For a string called `a_string`, `find()` can be used in the following way:

`a_string.find(substring, start, end)`

- `substring` is what we are searching for.
- `start` is the index from which we start searching in `a_string`.
- `end` is the index where we stop our search in a `a_string`.

`start` and `end` are optional.

```
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range
```

# Replace

`replace()`

`a_string.replace(substring_to_replace, new_string)`

The original string is not altered, instead a new string with the replaced substring is returned.

```
a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)
```

## Changing Letter Case

`upper()`

`lower()`

`my_string.upper()`
`my_string.lower()`

# Type Conversions

*To int* --> `int()`

`int()`

```
print(int("12") * 10)  # String to integer
print(int(20.5))  # Float to integer
print(int(False))  # Bool to integer

# print (int("Hello")) # This wouldn't work!
```

`ord()`

Convert a character to its Unicode value.

```
print(ord('a'))
print(ord('0'))
```

`float()`

Translates data into a floating-point number.

```
print(float(24))
print(float('24.5'))
print(float(True))
```

`str()`

Convert data into a string.

```
print(str(12) + '.345')
print(str(False))
print(str(12.345) + ' is a string')
```

`bool()`

Takes in data, and returns the corresponding Boolean value.

Strings are always converted to `True`.
Floats and Integers with the value of `0` are considered to be `False`.
All other terms are `True`.

```
print(bool(10))
print(bool(0.0))
print(bool("Hello"))
```

Other conversions are:

`complex()` and `hex()`

# Lambda Functions

> A lambda is an anonymous function (without a defined name) that *returns* some form of data.

> Can be written in-line, which isn't a huge advance

> They are particularly useful when a function requires another function as its argument!

`*lambda* parameters : expression`

parameters --> inputs to the lambda function

expression --> operation that returns something

```
triple = lambda num : num * 3

print( triple(10) ) # calling the lambda and giving it a parameter
```

```
concat = lambda a,b,c : a[0] + b[0] + c[0]

print( concat("World", "Wide", "Web") )
```

# Functions as arguments

Make a `calculator` function

```
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

###################################

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)

print(calculator(lambda n1, n2: n1 + n2, 10, 20))
```

# The `Map()` function 

The `map()` function, creates a map object using an existing list, and a function as its parameters.

This object can be converted to a list using the `list()` function.

`map(function, list)`

The `function` will be applied, or *mapped* to all the element of the `list`.

Below, we'll use the `map()` to double the values of an existing list:

```
num_list = [0,1,2,3,4,5]

double_list = map(lambda n:n *2, num_list)

print( list(double_list) )
```

This creates a new list! The original list remains unchanged.

We could have created a function that doubles a number and used it as the argument in `map()`, but the lambda made things simpler.

# `Filter()` Function

Another similar example is the `filter()` function. Requires a function and a list.

`filter()` *filters* elements from a list, if the elements satisfy the condition that is specified in the argument function!

For instance, we can write a `filter()` function that filters all the elements which are greater than `10`:

```
numList = [30,-2,-15,17,17,9,100]

greater_than_10 = list( filter(lambda n: n > 10, numList))
# Lambda: returns value of "n" if n > 10
```

`filter()` function returns a **filter object** which can be converted to list using `list()`.

Just like `map()`, `filter()` returns a new list without changing the original one.

Thus, we can see how functions can become arguments, and why lambdas are useful within functions, and can be used as mapping/filtering functions.

# Recursion

The process in which a function calls itself during its execution, each recursive call takes the program one scope deeper into the function.

The recurve call stops at the **base case**. The base case is a check used to indicate that there should be no further recursion.

Each recursion call is the general (recursive) case/step, where the solution is expressed in terms of a smaller version of itself. 

```
def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5)
```

In each call, the value of the number variable is printed. We then check whether the base case has been fulfilled. If not, we make a recursive call to the function with the current value decremented.

One thing to notice is that an outer call cannot move forward until all the inner recursive calls have finished. This is why we get a sequence of 5 to 0 to 5.

# Why use Recursion?

Allows us to easily solve many problems related to **graphs** and **trees**, and important in search algorithms.

If we don't specify an appropriate base case, or update our arugments as we recurse, the program will reach **infinite recursion** (and eventually crash).

The arguments passed to our recursive function are updated in each recursive call, so that base case can eventually be reached.



