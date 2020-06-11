# Python Classes

Object-Oriented Programming (OOP)

Class is a structure that allows you to group together a set of properties (called attributes), and functions (called methods or subroutines), to manipulate those properties.

Most classes will need the CONSTRUCTOR method `(__init__)` to **initialize** the class's attributes. A constructor will receive arguments, and stores that information in the **class's instance** (referenced by the `self` keyword). 

# Python Data Model - Built-in Methods (Dunder Methods)

Python has many built-in methods (Dunder methods)

https://docs.python.org/3/reference/datamodel.html

Python has a built-in method `__str__` used for the string representation of an object.
By default, when an object is printed, Python returned the memory address in which the object is stored.

Another built-in method is `__repr__`, which is similar to `__str__`. 

Both of them can be overridden for any clasas, and there are only minor differences.

### object.`__repr__` 
Called by the repr() built-in function to compute the "official" string representation of the object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value. 

The result value MUST be a string object. If a class defines `__repr__()` but not `__str__()`, then `__repr__()` is also used when an "informal" string representation of instance sof that class is required. 

> This is typically used for debugging, thus important that the representation is INFORMATION-RICH an UNAMBIGIOUS

### object.`__str__`

Called by `str(object)` and the built-in functions `format()` and `print()` to compute the "informal" or nicely printable string representation of an object. The result value must be a string object. 

This method differs from `object.__repr__()` in that there is NO EXPECTATION that `__str__()` returns a valid Python expression. That is, a more convenient or concise representation can be used. 

The default implementation defined by the built-in type `object` calls `object.__repr__()`.

### Summary between str() and repr()

`str()`
1) Makes the object readable
2) Generates output for the end-user

`repr()`
1) needs code that reproduces the object
2) generates output for the developer

If both methods are defined in a class, then `__str__` is used.

# Python Inheritance

Inheritance is a process in which a **subclass** can *inherit* the attributes and methods of another class, allowing it to rewrite some of the **super class**'s functionalities (in other languages, called the **parent class**)

For instance, the `person` class in the first lesson could permit us to create a subclass for people at 10 years of age.

```
class Person:
      def __init__(self, name, age): # Person's constructor
          self.name = name # Person's attribute
          self.age = age # Person's attribute

      def greet(self): # Person's method
          print("Hello, my name is %s!" % self.name)

class TenYearOldPerson(Person): # TenYearOldPerson inherits from Person

      def __init__(self, name): # TenYearOldPerson's constructor
          Person.__init__(self, name, 10) # accesses Person's constructor

      def greet(self): # rewrites the greet method
          print("I don't talk to strangers!!")

tyo = TenYearOldPerson("Jack") # instance of TenYearOldPerson
tyo.greet() # call greet method of the TenYearOldPerson
```

# Python Multi-Level Inheritance

**Organization of Super, Subclass and Sub-Subclasses**

Animal | Mammal | Carnivore
---|---|---
Superclass | Subclass | Sub-Subclass

**Relation between Class Types**

Class | Superclass | Relation
---|---|---
Carnivore | Mammal | Carnivore is a Mammal
Mammal | Animal | Mammal is an Animal
Animal | - | -



