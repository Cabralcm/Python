# Python Exercise
# Multiple Asynchronous Calls

# Change the previous program to schedule the execution of two calls to the sum function
import asyncio

async def get_sum(n1,n2):
    print(f"Sum Number: {n1} + {n2}")
    res = n1 + n2
    await asyncio.sleep(res)
    print(f"End Sum: {n1} + {n2}")
    return res

# Create Event Loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    get_sum(1,0),
    get_sum(1,1),
    get_sum(1,2)
))

print(results)

# Close the loop
loop.close()

# Official Solution

import asyncio

async def async_sum(n1,n2):
    print(f"Input: {n1},{n2}")
    res = n1 + n2
    await asyncio.sleep(1)
    print(f"Output: {res}")
    return res

loop = asyncio.get_event_loop()

results = loop.run_until_complete(asyncio.gather(
    async_sum(1,2),
    async_sum(1,3),
    async_sum(1,4)
))
print(results)

# Close the loop
loop.close()

'''
OUTPUT

Sum numbers 2 + 3
Sum numbers 3 + 4
Sum numbers 1 + 2
End Sum 2 + 3
End Sum 3 + 4
End Sum 1 + 2
[3, 5, 7]
'''

# Async outline

"""
import asyncio

async def sum_async(n1,n2):
    await asyncio.sleep(1)
    return

loop = asyncio.get_event_loop()

results = loop.run_until_complete(asyncio.gather(
    sum(n1,n2),
    sum(n1,n2),
    sum(n1,n2)
))

loop.close()
"""

"""
import asyncio

async def sum(n1,n2):
    print("Input")
    await asyncio.sleep(1)
    print("end")
    return n1+n2

loop = asyncio.get_event_loop()

results = loop.run_until_complete(gather(
    sum(1,1),
    sum(1,2),
    sum(1,3)
))

print(results)

loop.close()
"""