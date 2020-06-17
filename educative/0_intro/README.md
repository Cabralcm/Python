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



















