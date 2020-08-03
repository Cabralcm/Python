# Algorithmic Complexity

## Time and Space
- Time Complexity - The amount of time it takes for an algorithm to solve a given problem (or finish a routine)
- Space Complexity - The amount of space (memory, either primary or secondary, or tertiary) to solve a given problem

1) Types of input - we cannot directly compare in the general case for all algorithms to be A/B tested with every type of input
2) Algorithmic implementation - the same algorithm can be coded in many different ways, as well as optimized for the hardware or by the compiler
3) The program/software running the algorithm should be tested on the exact same hardware and software environment. Even if run on the same machine, the best algorithm might encounter an excessive amount of hardware interrupts. Thus impossible to guarantee the same hardware/software environment will ensure a fair comparison

# Analytical Evalution

 Must compare algorithms for:
1) Same input size
2) Consider all possible inputs of the given size

Hypothetical computer - primitive operations are computed in constant time

Specific input time, *n*. And count the number of primitive operations executed by an algorithm for a given input.

The algorithm that results in fewer primitive operations is considered better.

Primitive operations - Processor instructions (assignment to variable, array index, reading from variable or array index, comparing two values, arithmetic operations).

Not considered a primitive operation? -- Function call, when it is called, all the statements in that function are executed. Thus each function invocation is not a single primitive operation. 
Likewise displaying an entire array is not a primitive operation.

The number of times conditional statements run are dependent upon real input values. Code block is sometimes executed or not. How do we account for this?
1) Best Case analysis
2) Average Case Analysis
3) Worst Case analysis

##  Best Case Analysis
- Fewest possible primitive operations

Consider the specific input that results in the execution of the fewest primitive operations. This gives us a **lower bound** on the execution time of that algorithm for a given input size.

## Worst-Case analysis
- Maximum/most possible primitive operations

Consider the specific input that results in the execution fo the maximum number of primitive operations. This gives us an **upper bound** on the execution time of that algorithm for a given input size.



