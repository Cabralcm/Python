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








