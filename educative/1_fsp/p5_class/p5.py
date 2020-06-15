# Python Classes

class Person:
    
    MAX_AGE = 200 #Class constant (global class variable for all instances of the class)
    
    def __init__(self, name, age):
        self.name = name #class variable
        self.age = age
    
    def greet(self):
        print("Hello, my name is %s!" %self.name)

class Rectangle:

    def __init__(self, x1,y1, x2,y2):
        if (x2 > x1 and y1> y2):
        #Real monitors go by upper left corner as (0,0)
        #if(x2 > x1, and y2>y1):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

            self.top_left = (self.x1, self.y1)
            self.bottom_right = (self.x2, self.y2)
        else:
            print("Incorrect coordinates of the rectangle!")

    def width(self):
        return self.x2 - self.x1
    
    def height(self):
        return self.y1 - self.y2
    
    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return 2*self.width() + 2*self.height()

    def __str__(self): ##Overwrites the str output for the object when using print!
        # return str(self.x1) + "," + str(self.y1) + "," + str(self.x2) + "," + str(self.y2)
        return f"{self.x1},{self.y1},{self.x2},{self.y2}"

    def __repr__(self):
        # return str(self.x1) + "," + str(self.y1) + "," + str(self.x2) + "," + str(self.y2)
        return f"{self.x1},{self.y1},{self.x2},{self.y2}"


r = Rectangle(2,7,8,4)
print(r.width())
print(r.height())
print("Area: " + str(r.area()))
print("Perimeter: " + str(r.perimeter()))
print(r)

# Inheritance Example

class Person:

    def __init__(self, name, age): #Person's constructor
        self.name = name #Person's field/attribute
        self.age = age #Person's field/attribute
    
    def greet(self): #Person's method
        print(f"Hello, my name is {self.name}!")

class TenYearOldPerson(Person): # TenYearOldPerson Inherits from Person

    def __init__(self,name): #TenYearOldPerson's constructor
        Person.__init__(self, name, 10) # accesses Person's Constructor
    
    def greet(self): #Rewrites (overriding) the greet method
        print("I don't talk to strangers!")

tyo = TenYearOldPerson("Jack") #instance of TenYearOldPerson
tyo.greet() # call greet method of the TenYearOldPerson

### Classes and Sub Classes

class Animal():
    def __init__(self, name, food, characteristic): # Animal's constructor
        self.name = name # Animal's attribute
        self.food = food # Animal's attribute
        self.characteristic = characteristic # Animal's attribute
        print("I am a " + str(self.name) + ".")
    
class Mammal(Animal): # Mammal inherits from Animal
    def __init__(self, name, food): # Mammal's constructor
        Animal.__init__(self, name,food, "warm blooded") #Animal's constructors
        print("I am warm blooded.")

class Carnivore(Mammal):
    def __init__(self, name): #Carnivore inherits from Mammal
        Mammal.__init__(self, name, "meat") #Mammal's constructor
        print("I eat meat.")

lion = Carnivore("lion") # Lion is an instance of a Carnivore

### Multi-Inheritance (Chained Inheritance)

class Animal():
    def __init__(self, name, food, characteristic): # Animal's constructor
        self.name = name # Animal's attribute
        self.food = food # Animal's attribute
        self.characteristic = characteristic # Animal's attribute
    def printer(self):
        print("I am a " + str(self.name) + ".")
    
class Mammal(Animal): # Mammal inherits from Animal
    def __init__(self, name, food): # Mammal's constructor
        Animal.__init__(self, name,food, "warm blooded") #Animal's constructors
    def printer(self):
        print("I am warm blooded.")

class Carnivore(Mammal):
    def __init__(self, name): #Carnivore inherits from Mammal
        Mammal.__init__(self, name, "meat") #Mammal's constructor
    def printer(self):
        print("I eat meat.")

lion = Carnivore("lion")
lion.printer()

### Multiple Inheritance (Parallel Inheritance)

class Person:
  def __init__(self, name):
      self.name = name

  def greet(self):
    print("Hi, I am " + self.name + ".")


class Student (Person): # Student inherits from Person class
  def __init__(self, name, rollNumber):
    self.name = name # Attribute inherited from the Person class
    self.rollNumber = rollNumber # Student's attribute
    Person.__init__(self, name) # Person's constructor

  def report(self): # Student's method
    print("My roll number is " + self.rollNumber + ".")

class Teacher (Person): # Teacher inherits from Person class
  def __init__(self, name, course):
    self.name = name # Attribute inherited from the Person class
    self.course = course # Teacher's attribute
    Person.__init__(self, name) # Person's constructor   

  def introduce(self): # Teacher's method
    print("I teach " + self.course + ".")

class TA (Student, Teacher): # TA inherits from Student and Teacher class
  def __init__(self, name, rollNumber, course, grade):
    self.name = name # Attribute inherited from the Person class
    self.rollNumber = rollNumber # Attribute inherited from the Student class
    self.course = course # Attribute inherited from the Teacher class
    self.grade = grade # TA's attribute
    
  def details(self): # TA's method
    if self.grade=="A*" or self.grade=="A" or self.grade=="A-": # if person is elligible for TAship
      Person.greet(self) # can access Person's greet method
      Student.report(self) # can access Student's report method
      Teacher.introduce(self) # can access Teacher's introduce method
      print ("I got an " + self.grade + " in " + self.course + ".")
    else: # person is not elligible for TAship
      print(self.name + ", you can not apply for TAship.")
    
ta = TA('Ali', '13K-1234', 'Data Structures' ,'A') # TA object
ta.details()

#uncomment any of the following lines of code and see how they work
# ta.greet()
# ta.report()
# ta.introduce()

print("\n")

ta2 = TA('Ahmed', '14K-5678', 'Algorithms' ,'B')
ta2.details()

### Super Method

# Inheritance without Super

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

## Inheritance WITH Super

class Person(object): # Super class
  def __init__(self, name):
    self.name = name
  def greet(self):
    print ("Hi, I'm " + self.name + ".") # Super class does something

class Student(Person): # Subclass inheriting from the super class
  def __init__(self, name, degree):
    self.name = name
    self.degree = degree
    super().__init__(name) # calls constructor of super class
  def greet(self):
    super().greet() # calls method of super class
    print ("I am a " + self.degree + " student.")
  
student = Student("Ali", "PhD") # Create an object of the subclass
student.greet()

## Challenge - Rectangle Class

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return self.x2 - self.x1
    
    def height(self):
        return self.y1 - self.y2
    
    def perimeter(self):
        return sum(self.x1, self.x2, self.x3, self.x4)
    
    def area(self):
        return self.width() * self.height()

## My solution --> did not call Super()....

class Square():

    def __init__(self, x1, y1, length):
        self.x1 = x1
        self.y1 = y1
        self.length = length
    
    def get_length(self):
        return self.length

    def area(self):
        return self.get_length()**2

class Square(Rectangle): #Inately inherits the methods from the Rectangle class!

    def __init__(self,x1,y1,length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1,y1,x2,y2) #Calls the Rectangle Constructor!

## Inheritance Solution

class Square(Rectangle):

    def __init__(self, x1, y1, length):
        x2 = x1 + length #Top left corner for a screen, bottom left for a graph
        y2 = y1 + length #Top left corner for a screen, bottom left for a graph
        super().__init__(x1,y1,x2,y2) #Note, we don't need to call SELF when using the super() function

# Testing the code

s = Square(1,1,10)
print(f"Width: {str(s.width())}, Height: {str(s.height())}, Area: {str(s.area()}")

s2 = Square(2,5,7)
print(f"Width: {str(s.width())}, Height: {str(s.height())}, Area: {str(s.area()}")




