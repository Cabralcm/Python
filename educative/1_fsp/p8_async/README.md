# Python Asynchronous Progamming

## Synchronous programming

Synchronous program execution is straightforward: a program starts at the first line, then each line is executed until the program reaches the end. Each time a function is called, the program waits for the function to return before continuing to the next line.

## Asynchronous Programming

Asynchronous progrmaming allows you to write concurrent code that runs in a single thread!

# Concurrency

Scenario: Reading a novel while painting. Even if it *seems* you are doing two tasks at the same time, what you are doing is switching between the two tasks. While you wait for the paint to dry, you are reading your novel. But while you are painting, you also pause your reading. This is called **concurrency**.

A single thread allows you to decide where the scheduler will switch from one task to another, which means that sharing data between tasks is *safer* and *easier*. 

A thread is where there is shared memory between other active threads.

A process does not have the shared memory (or objects such as variables) that is possible with a thread. However, this separation may be desired.

## Minimum Memory Usage

Every time a new thread is created, some memory is used to allow context switching. If we use async programming, there is no a problem since the code runs in a single thread.

# Python Asynchronous Code

To write asynchronous code in Python, import the library using `import asyncio`

**Components**

`Asyncio` has 3 main components
1) co-routines
2) event loop
3) future

## Coroutine

A coroutine is the result of an asynchronous function which can be declared using the keyword `async` before `def`, for a normal function call.

```
async def my_function(argument):
    pass
```

when we declare a function using the async keyword, the function is not executed, insetad a coroutine object is returned.

To call a coroutine, we write:

```
my_coroutine = my_function(argument)
```

There are TWO ways to read the output of an async function from a coroutine. The first way is to use the `await` keyword, which is only possible inside async functions. It will wait for the coroutine to terminate and return the result.

```
result = await my_function(argument)
```

The second way is to add it to an event loop!

# Event Loop

The event loop is the boject whic hexecutes our synchronous code, and decides how to switch bewteen aync functoins. After creating an event loop we can add multiple coroutines to it; these coroutines will all be running concurently when `run_until_complete` or `run-forever` is called.

```
loop = asyncio.new_event_loop() # create event loop
future = loop.create_task(my_coroutine) # add coroutine to the loop
loop.run_until_complete(future) # add coroutine to the loop concurrently 
loop.close()
```

`loop.create_task()` --> creates the task to be accessable by the loop

`loop.run_until_complete` --> loop concurrently executes the task/coroutine until complete

# Future

A future is an object that works as a placeholder for the output of an asynchronous function, and it **give us information about the function state**. 
A future is created when we add a coroutine to an event loop.

There are two ways to accomplish this:

`future = loop.create_task(my_coroutine)`

The method adds a coroutine to the loop, and returns a task which is a subtype of the future.

In **asynchronous programming**, the execution of a funciton is usually non-blocking. 
That is, each time you call a funciton, it returns immediately. However, that function does not necessarily get executed right away. 
Instead, there is usually a mechanism (called the "scheduler"), which is responsible for the future execution of the function.

The problem with asynchronous programming is that a program may end before any asynchronous function starts.
A common solution for this is for asynchronous functions to return "futures" or "promises".These are objects that represent the state of execution of an async function. 
Finally, asynchronous programming frameworks typically have mechanisms to block or wait for those async functions to end based on those "future" objects. 

# Co-operative Multitasking

Since Python 3.6, the `asyncio` module combined with the `async` and `await` keyboard allows us to implement what is called *co-operative multi-tasking programs*. 
In this type of programming, a couroutine function voluntarily yields control to another coroutine function when idle or when waiting for some input.

Asynchronous functions are declared with `async def`.

```
import asyncio
async def functionName():
    await asyncio.sleep(1)
    return
```

During the sleep() function call, due to using `await` this function will yield control and allow other functions to be run.

# Execute a Single Task

To call an asynchronous function once, do the following:
1) Create an Event Loop
2) Run async function and wait for completion
3) Close the Loop

```
# Create an event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(functionName())

# Close the loop
loop.close()
```

Consider the following asnchronous function that squares a number and sleep for one second before returning. (Ignore the `await` keyword for now).

```
import asyncio

async def square(x):
    print("Square", x)
    await asyncio.sleep(1)
    print("End square", x)
    return x*x

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(square(1))
print(results)

# Close the loop
loop.close()
```

The event loop for [Asynchronous Programming](https://docs.python.org/3/library/asyncio-eventloop.html) is (among other things), the Python mechanism that schedules the execution of asynchronous functions. 
We use the loop to run the function until completion. 
This is a synchronizing mechanism that makes sure the next print statement doesn't execute until we have some results.

# Execute Multiple Tasks

The previous example is not a good example of asynchronous programming because we don't need that much complexity to execute only one function. 
However, imagine that you would need to execute the `square(x)` function three times like this:

```
square(1)
square(2)
square(3)
```

To call an asynchronous function to execute multiple tasks, do the following:
1) Create an event loop
2) Run async function and wait for completion

```
# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
functionName()
functionName()
.
.
.
functionName()))

# Close the loop
loop.close()
```

Since the `square()` function has a sleep function inside, the total execution time of this program would be 3 seconds. 
However, given that the computer is going to be idle for a full second each time the function is executed, why can't we start the next call while the previous is sleeping?

Here is how we accomplish this:

```
import asyncio

async def square(x):
    print("Square", x)
    await asyncio.sleep(1)
    print("End square", x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_completion(asyncio.gather(
    square(1),
    square(2),
    square(3)
))
print(results)

# Close the loop
loop.close()
```
**Output**
> Square 2

> Square 1

> Square 3

> End square 2

> End square 1

> End square 3

> [1, 4, 9]

We use `asyncio.gather(*tasks)` to inform the loop to wait for all tasks to finish. 
Since the coroutines wil start at almost the same time, the program will run for only 1 second.
Asyncio **gather()** won't necessarily run the coroutines by order, although it will return an ordered list of results.

Sometimes results may be neeed as soon as they are available. For that, we can use a second coroutine that deals with each result using `asyncio.as_completed()`:

```
import asyncio

async def square(x):
    print("Square", x)
    await asyncio.sleep(1)
    print("End square", x)
    return x * x

loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("Result:", await res)

loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))
```
**Output**
> Square 2

> Square 1

> Square 3

> End square 2

> End square 1

> End square 3

> Result: 4

> Result: 1

> Result: 9

Finally, async coroutines can call **other async coroutine functions** with the **await** keyword:

```
import asyncio

async def compute_square(x):
    await asyncio.sleep(1)
    return x * x

async def square(x):
    print("Square", x)
    res = await compute_square(x)
    print("End square", x)
    return res

# Create event loop
loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("Result:", await res)

loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))
```
**Output**
> Square 2

> Square 1

> Square 3

> End square 2

> End square 1

> End square 3

> Result: 4

> Result: 1

> Result: 9

