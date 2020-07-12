# Default Dict

'''
Subclass of Python's dict that accepts a default_factory as its primary argument

The default_factory is usually a Python type, such as int or list
can also use a function or a lambda too

Create  regulat Python dictionary that counts the number of times each word is used in a sentence
'''

from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)

# Using defaultdict
# words is a list of words

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

'''
Default dict automatically assigns ZERo as the value to any key it doesn't already have in it.
That is, when we perform the += 1 operation (when we add a one), it always starts from zero.
We add one so it makes more sense, and it will also increment if the word appears multiple times in the sentence
''' 

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}

for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]
print("Account Dictionary")
print(reg_dict)

# Using Default Dict

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print("Default Dict")
print(d)
print(d.items())

# Lambda Function

animal = defaultdict(lambda: "Monkey") #arugment being passed to the defaultdict is called your default_factory
# Essentially, by default any key that is added will have by default the value of "Monkey" assigned to it!
animal['Sam'] = 'Tiger'
print (animal['Nick'])
#Monkey

print (animal)
#defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})

'''
In case you haven’t noticed yet, it’s basically impossible to cause a KeyError 
to happen as long as you set the default_factory to something that makes sense. 
The documentation does mention that if you happen to set the default_factory 
to None, then you will receive a KeyError. 
'''

x = defaultdict(None) #This is a broken defaultdict!
x['Mike']
# It can no longer assign a default to our key, so it throws a KeyError instead.


