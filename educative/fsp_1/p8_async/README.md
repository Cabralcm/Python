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



