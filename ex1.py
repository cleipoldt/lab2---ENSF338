"""
Q1. This is a recursive implementation of the fibonacci sequence. When the function gets called with a random
value for n, if n is 0 or 1, the function returns either 0 or 1, depending on what the user inputed or called their function with.
If the value of n is anything other than 0 or 1, the function returns by recursively calling itself with input n-1, and n-2, and summing there results to properly compute the
fibonacci value for n.

Q2. Yes, this function uses the divide and conquer algorithm due to the fact it uses recursion and divides into two subproblems; however, it is very inefficient as it computes redundantly.
When it gets divided into two subproblems, the subproblems share certain overlapping calculations. So yes, but more like divide and conquer done incorrectly.

Q3. The expression for the time complexity is T(n) is O(2^n)

"""

"""
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    

for i in range(10):
    print(func(i))
"""

# Q4 Fibonacci implementation which uses Memoization

cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

print([fibonacci(n) for n in range(15)])