# Python Data Structures

1) List
2) Tuple
3) Dictionary (Hash Table/Map)
4) Set

Other data structures

5) Stacks
6) Queues
7) Trees (Binary, etc)
8) Graphs

And Custom data structures!


# Lists

`+` to merge two lists together.   

`extend()` to add the elements of one list at the end of another.

## Adding Elements - Append

`my_list.append(newElement)`

## Insert Method

`my_list.insert(index, newElement)`

If a value already exists at that index, the whole list from that value onwards will be **shifted one step to the right!**

## Removing elements

1) **Pop** `my_list.pop()` - Remove element, but makes it available to be assigned to a new variable

```
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
```

2) **Remove** `my_list.remove( element_to_be_deleted)` - Remove element, only deletion, without making it available for assignment.

Note, we are NOT deleted at an index, we are searching for an element/value in the list that we wish to remove!

3) **DEL** -- `del my_list[index]` - Remove element by index 

OR

`del my_list[start:stop]` - Remove element by slice

## Index Search

**Index** -- `my_list.index(element)` - Input: Element/Value in the List, Returns: Index in which the element is stored!

**in** -- `print("London" in my_city_list)`

## List Sort






