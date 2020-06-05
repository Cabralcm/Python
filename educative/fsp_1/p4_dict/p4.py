# Dictionaries

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

#print one item
# print("Get age of Peter")
# print(ages["Peter"])

## Print the whole dictionary
# print("Get the age of all persons")
# for key,value in ages.items():
    # print(f"Person:{key} , Age: {value}")

## Call dictionary with no parametes using the dict keyword
new_dict = dict()
# Alternatively
new_dict = {}

# For instance:
ages = dict()
ages['Peter'] = 12
ages['Susan'] = 13
# for key, value in ages.items():
    # print(key,value)

from collections import OrderedDict

ages = OrderedDict()

ages['Peter'] = 12
ages['Susan'] = 10
ages['Maria'] = 5
  
# for key, value in ages.items(): 
    # print(key, value) 

# Recall, the dictionary isn't necessarily printed in the order it was saved!

# We can use:
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

"""
for x in ages:
  print(x)

for x in ages.values():
  print(x)

for x in ages:
  print(ages[x])
  print(ages.get(x))

for name,age in ages.items():
    print(name,age)
"""

# Dictionary keys can also contain dictionaries

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(students) #Looks like JSON!
print(students['Peter'])
print(students['Peter']['address'])

for p_id, p_info in students.items():
    print("\nPerson Name:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])

# Useful to store heirarchical information