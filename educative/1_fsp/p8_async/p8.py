# Python Asynchronous

# Problem 1
"""
Implement an asynchronous coroutine function to add two variables, 
and sleep for the duration of the sum.

Use the asyncio loop to call the function with two numbers.
"""

import asyncio

# async def async_sun(n1,n2):


# async def sum(n1,n2):
#     res = n1 + n2
#     await asyncio.sleep(res)
#     return res

# loop = asyncio.get_event_loop()

# results = loop.run_until_complete(asyncio.gather(
#     sum(1,2),
#     sum(1,3),
#     sum(1,4)))
# print(results)

# Formal Solution

# import asyncio

# async def sumNumbers(n1,n2):
#     await asyncio.sleep(1)
#     return

# # Call the asynchrnous coroutine

# # Step 1 - Create an event loop
# loop = asyncio.get_event_loop()

# # Step 2 - Run Async function and wait for completion

# results = loop.run_until_complete(sumNumbers(1,1))

# # Step 3 - Close the loop

# loop.close()

# Example Code

import asyncio

async def get_sum(n1,n2):
    print("Sum Number", n1, "+", n2)
    await asyncio.sleep(1)
    print("End Sum", n1, "+", n2)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()
n1 = 1
n2 = 2
# Run async function and wait for completion
results = loop.run_until_complete(get_sum(n1,n2))
print("Sum of two numbers:", n1, "+", n2, "=", results)
print(f"Sum of two numbers: {n1} + {n2} = {results}")

loop.close()

