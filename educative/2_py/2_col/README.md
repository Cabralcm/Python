# Python Containers

Containers can be used to replace Python's default: `dict,tuple,list and set`

1) Chainmap
2) DefaultDict
3) deque
4) namedtuple
5) OrderedDict

| method | function|
|---|---|
| namedtuple()  | factory function for creating tuple subclasses with named fields
| deque         | list-like container with fast appends and pops on either end
| ChainMap      | dict-like class for creating a single view of multiple mappings
| Counter dict  | subclass for counting hashable objects
| OrderedDict   | dict subclass that remembers the order entries were added
| defaultdict   | dict subclass that calls a factory function to supply missing values 
| UserDict      | wrapper around dictionary objects for easier dict subclassing
| UserList      | wrapper around list objects for easier list subclassing
| UserString    | wrapper around string objects for easier string subclassing

# ChainMap

A class that provides the ability to link multiple mappings together such they end up being a single unit.

It accepts **maps**, which means that a ChainMap will accept any number of mappings or dictionaries, and turn them into a single view that you can update.

## Purpose

Useful if you want to set up defaults. 

Create application that has some defaults. The application will also be aware of the OS's environment variables.

If an enviroment variable that matches one of thekeys that we are defaulting to in our application, the enviroment will override our default. 

If we can pass arguments to our application, these arguments take precedence over the envirnment and the deafults. 

> See p2.py

Python `vars()` - Returns the **\_\_dict\_\_** attribute of the given object.


```
import argparse
import os

from collections import ChainMap


def main():
    app_defaults = {'username':'admin', 'password':'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value 
                              in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ, 
                     app_defaults)
    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()


if you pass the terminal:
python3 chain_map.py -u mike

You will get *mike* back twice! 

This is because the command line arguments overrides everything else, itd oesn't matter that we set the environment because our ChainMap will oook at the command line arguments first before anything else.
```
1) Set up Argparse, tell it to handle certain command line options
2) Argparse doesn't provide a way to get a dictionary objects of its arguments, so we just use a dict comprehension to extract each of the key:value pairs from the argparse
3) `vars()` function returns the __dict__ attribute of the given object --> `vars(args) == args.__dict__`

> The `vars()` function returns the \_\_dict\_\_ attribute of the given object. 

If the `vars()` function is not given any arguments, instead it functions like the `locals()` method. `locals()` returns:
- A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.

a) Global symbol table
b) Local symbol table

`Chainmap` - is a class that provides the ability to link multiple mappings together such that they end up being a single unit (dictionary, or object).

Chainmap accepts `maps` as arguments, that is any number of mappings or dictionaries, and turns them into a single view that you can update.

```
from collections import ChainMap
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print (car_pricing['hood'])
```

# Counter

Convenient and fast tallies, called `Counter`. Run it against most iterables.

```
from collections import Counter
print (Counter('superfluous'))
#Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = Counter('superfluous')
print (counter['u'])
#Output: 3
```

`Counter()` will allow us to count the occurances of each of the unique iterables, and create key:value pairs for the iterable:occurances for each iterable. Stored in a dictionary.

We can call *elements* which will run an 






