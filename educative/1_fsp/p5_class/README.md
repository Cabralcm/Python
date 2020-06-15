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

**Multi-Level inheritance in Python, which is similar to single-level inheritance**

```
class Animal ():
  def __init__(self, name, food, characteristic): # Animal's constructor
    self.name = name # Animal's attribute
    self.characteristic = characteristic # Animal's attribute
    self.food = food # Animal's attribute
    print ("I am a " + str(self.name) + ".")
    
class Mammal (Animal): # Mammal inherits from Animal
  def __init__(self, name, food): # Mammal's constructor
    Animal.__init__(self, name, food, "warm blooded") # Animal's constructor
    print ("I am warm blooded.")
    
class Carnivore (Mammal): # Carnivore inherits from Mammal
  def __init__(self, name): # Carnivore's constructor
    Mammal.__init__(self, name, "meat") # Mammal's constructor 
    print ("I eat meat.")

lion = Carnivore("lion") # lion is an instance of Carnivore
```
Adding a `printer()` method for each Class

```
class Animal ():
  def __init__(self, name, food, characteristic):
    self.name = name
    self.characteristic = characteristic
    self.food = food
  def printer(self):
    print ("I am a " + str(self.name) + ".")
    
class Mammal (Animal):
  def __init__(self, name, food):
    Animal.__init__(self, name, food, "warm blooded")
  def printer(self):
    print ("I am warm blooded.")
    
class Carnivore (Mammal):
  def __init__(self, name):
    Mammal.__init__(self, name, "meat")
  def printer(self):
    print ("I eat meat.")

lion = Carnivore("lion")
lion.printer()
```

If you remove `printer()` method of the Carnivore class, `lion` object will be able to access the `printer()` method of its super/parent class `Mammal`. This output would be:

`I am warm blooded.`

Since it belongs to the Mammal class.

If you remove the `printer()` method of the Mammal class, the `lion` object will access the `printer()` method of its superclass `Animal`. Thus removing both `printer()` methods of the Mammal and Carnivore class. Thus the `Carnivore` class will merely inherit `printer()` from the `Animal` superclass. No overwriting will occur. The output would be:

`I am a lion.`

# Python Multiple Inheritance

In Python, a class can inherit **attributes** and **methods** from **more than one class.**

Critics of multiple inheritance say that it is confusing and complex. Such as the [Diamond Problem](https://en.wikipedia.org/wiki/Multiple_inheritance).

The idea that Multiple Inheritance is somehow "bad" is mainly based on the fact that some languages either do not support multiple inheritance (like Java), or do not have a very good implementation for it. Python however has a very sophisticasted and well-structured approach to multiple inheritance.

Consider the following code snippert where `ChildClass` inherits from `ParentClass1, ParentClass2, ParentClass3`, and so on.

```
class ChildClass(ParentClass1, ParentClass2, ParentClass3, ...):
    pass
```

## Multiple Inheritance Example

Real-world example, where a `person` can be either a `Teacher` or a `Student`.
Additionally, a `person` can be a `TA`. A `TA` inherits the attributes and methods of both the `Student` and `Teacher` class because, essentially, a `TA` is a `Student`, who is performing some of the duties that a `Teacher` performs. That is, a diamon structure:

| |Person| |
--|--|--
Student| |Teacher|
| |TA| |

Where, `Person` contains: name, and greet()

`Student` contains: name, rollNumber, and greet(), report()

`Teacher` contains: name, course, and greet(), introduce()

`TA` contains: name, rollNumber, course, grade, and greet(), report(), and introduce()

# Python Super Method - Inheritance

You can access the constructor and methods of the parent class from the child class using:

`ParentClassName.__init__(self, methodParameter)` 

`ParentClassName.__init__(self, methodParameter)`

This method tends to be confusing when the hierachy has multiple levels because you have to remember the exact names of the parent classes and where to use them. 

An easier way to do this is the `super()` method.

The built-in `super` function allows the child class (or subclass) to access inherited methods of the parent class (or superclass) that have been overwritten in the child class.

[Python Docs for Super Function](https://docs.python.org/2/library/functions.html#super)

> Super is used to return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have overriden in a class.

## Using the `Super` Function

1) Single Inheritance
- We can use `super` in single inheritance to refer to the parent (or super) class or multiple classes without explicitly naming them. This is just a shortccut and helps make your code maintainable and easy to understand.

2) Multiple Inheritance
- it is possible in Python for a class to inherit from multiple parent classes. You can use the `super` method to multiple or collaborative inheritance. This can be done only in Python (or languages the same capabilities) because some languages do not support inheritance from multiple classes.

## Syntax for `Super`

`super().methodName(args)`

Following example where the `Student` class inherits from (or "is a") `Person`.

```
class Person(object): # Super class
  def __init__(self, name):
    self.name = name
  def greet(self):
    print ("Hi, I'm " + self.name + ".") # Super class does something

class Student(Person): # Subclass inheriting from the super class
  def __init__(self, name, degree):
    self.name = name
    self.degree = degree
    Person.__init__(self, name) # calls constructor of super class
  def greet(self):
    Person.greet(self) # calls method of super class
    print ("I am a " + self.degree + " student.")
  
student = Student("Ali", "PhD") # Create an object of the subclass
student.greet()
```

Notice, when you create a `Student` object, it can access the `Parent` class's `greet()` method and write its own too.

```
class Person(object): # Super class
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hi, I'm {self.name}.") # Super class does something

class Student(Person): # Subclass inheriting from the super class
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
        super().__init__(name) # calls the constructor of the super class
    def greet(self):
        super().greet() # calls method of super class
        print(f"I am a {self.degree} student.")

student = Student('Ali','PhD')
student.greet()
```

> Important - in the code sample above, when we called the parent class's methods `super().__init__(name)` and `super().greet()`, we didn't explictly add `self` as a parameter to these methods.

