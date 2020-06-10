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

for x in ages.keys():
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
'''
print(students) #Looks like JSON!
print(students['Peter'])
print(students['Peter']['address'])

for p_id, p_info in students.items():
    print("\nPerson Name:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])
'''

# Useful to store heirarchical information

# Length of Dictionary

def lengthDictionary(students):
    length = 0
    for x in students.keys():
        length += 1
    return length

def lengthDictionary2(students):
    return sum(students.keys())

def lengthDictionary3(students):
    return sum(students)

# Average of Values of Keys in a Dictionary

def calculateAvg(ages):
    total_keys = len(ages)
    sum_ages = sum(ages.values())
    return sum_ages / total_keys

def calculateAvg2(ages):
    total_keys = 0
    sum_ages = 0
    for k,v in ages.items():
        total_keys += 1
        sum_ages += int(v)
    return sum_ages / total_keys

def calculateAvg3(ages):
    return ( sum(ages.values()) / len(ages))

# print(calculateAvg3(ages))

## Return Key with Maximum Value
# Returns the name of the Oldest Student

def oldestStudent(ages):
    # rev_dict = {v:k for k,v in ages.items()} #This does not work if there are students with the same age!
    c_name = ""
    c_max = 0
    max_val = max(rev_dict.keys())
    for k,v in ages.items():
        if v > c_max:
            c_max = 0
            c_name = k
    return c_name

def oldestStudent2(ages):
    values = list(ages.values()) 
    keys = list(ages.keys())
    # key_index = values.index(max(values))
    return keys[values.index(max(values))]

def oldestStudent3(ages):
    values = list(ages.values())
    keys = list(ages.keys())
    key_index = values.index(max(values))
    keys[key_index]

# oldestStudent(ages)

# Increment Dictionary Values

def updateAges(ages, n):
    ages = {k:v+n for k,v in ages.items()}
    return ages

def updateAges2(ages, n):
    for k,v in ages.items():
        ages[k] = v + n
    return ages

# print(updateAges2(ages,700))

# Total Students

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

def totalStudents(students):
    count = 0
    for x in students:
        count += 1

def totalStudents2(students):
    return len(students)

def totalStudents3(students):
    return (len(students.keys()))
    
# print(totalStudents2(students))

# Average Values within Multiple Dictionaries

def calculateAvgAge(students):
    num = len(students)
    total = 0
    for n in students.values():
        total += n["age"]
    print(total/num)
    return total/num

def calculateAvgAge2(students):
    add_age = 0
    for n in students.values():
        add_age += n["age"]
    return (add_age / len(students.keys()))

# calculateAvgAge(students)

def find_students(students, address):
    s_info = list(students.values())
    s_names = list(students.keys())
    print(s_names)
    indexes = [num for num,info in enumerate(s_info) if info['address'] == address]
    print(indexes)
    output = [[s_names[i]] for i in indexes]
    print(output)
    # print(values)
    # reside = [x for x in values if values["address"]==address]
    # print(reside)

# find_students(students, 'Lisbon')

def find_students2(students, address):
    names = []
    for key, subdict in students.items():
        for sublist in students.values(): #iterates through every entry in subdict
            if (sublist == address):
                names.append(key)
    return sorted(names)

def find_students3(students, address):
    names = []
    for key, subdict in students.items():
        if (subdict["address"] == address):
            names.append(key)
    return sorted(names)


