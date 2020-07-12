from collections import namedtuple

parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = parts(id_num = '1234', desc= 'Ford Engine', cost = 1200.00, amount= 10)
print(auto_parts.id_num)
print(dir(auto_parts))

# Standard Tuple

auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
print(auto_parts[2])
#1200.00

id_num, desc, cost, amount = auto_parts
print(id_num)


# using the named tuple approach, you can use Python's dir() method to inspect the tuiple and find out its properties!

# Convert Python dictionary int oan object

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
# create our namedtuple class, and name it Parts.
# The second arugment is a LIST of the keys from our dictionary.
# The last piece is this strange piece of code, (**Parts)
# The Double Asterisk means that we are calling our class using keywords arugments, which in this case is our dictionary. 
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)
#Parts(amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')

# We could split the double asterisk part into two lines to make it cleaner

parts = namedtuple('Parts', Parts.keys())
print(parts)

auto_parts = parts(**Parts)
print(auto_parts)

# Doing the same thing as before, we create the class first, then call the class with our dictionary to create an object

# Namedtuple also accepts a verbose argument, and a rename argument.

# The verbose arugment is a flag that will print out class definition right before it's built if you set it to True.
# The rename argument is useful if you're creating your namedtuple from a database or some other system that your 
# program doesn't control as it will automatically rename the properties for you!






 