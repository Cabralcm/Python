# deque

'''
 deques “are a generalization of stacks and queues”. They are pronounced “deck” which is short for "double-ended queue".
 '''

from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.append("bork")
print(d)

d.appendleft('TEST')
print(d)

d.rotate(1)
print(d)

d.rotate(-2)
print(d)

def get_last(filename, n=5):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

'''
Akin to Linux's TAIL program, pass in a filename to our script, along with the *n* number of lines we want returned.

The deque is bounded to whatever number we pass in as n

This means that once the deque is full, when new lines ar eread in and added to the deque

Order lines are popped off the other end, and discarded. I also wrapped the file opening *with* statement in a simple exception
handler because it's really easy to pass in a malformed path..

This will catch files that don't exist, or the filename is incorrect.
'''
