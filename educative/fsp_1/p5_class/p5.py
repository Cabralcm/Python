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

# Classes and Sub Classes

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




