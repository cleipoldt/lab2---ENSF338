"""
Q1. This is a recursive implementation of the fibonacci sequence. When the function gets called with a random
value for n, if n is 0 or 1, the function returns either 0 or 1, depending on what the user inputed or called their function with.
If the value of n is anything other than 0 or 1, the function returns by recursively calling itself with input n-1, and n-2, and summing there results to properly compute the
fibonacci value for n.

Q2. Yes, this function uses the divide and conquer algorithm due to the fact it uses recursion and divides into two subproblems; however, it is very inefficient as it computes redundantly.
When it gets divided into two subproblems, the subproblems share overlapping calculations. So yes, but it is more like divide and conquer done incorrectly.

Q3. The expression for the time complexity is T(n) is O(2^n) (exponential due to redundant recursive calls)

"""
import matplotlib.pyplot as plt
import timeit


# this function does not use memoization

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)



"""
Q4 Fibonacci implementation which uses Memoization
"""
cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

for i in range(35):
    print(fibonacci(i))
    
"""
Q5. The time complexity is now linear, T(n) is O(n) due to its avoidance in redundant recursive calls
"""

"""
Q6. The following is the timining and plotting implementation
"""

"""
Q6. The following is the timining and plotting implementation
"""

all_times_fast = []
for i in range(35):
    exec_time_fast = timeit.timeit(lambda: fibonacci(i), number = 1)
    all_times_fast.append(exec_time_fast)

all_times_slow = []

for i in range(35):
    exec_time_slow = timeit.timeit(lambda: func(i), number = 1)
    all_times_slow.append(exec_time_slow)


x_axis_fast = list(range(35))
plt.figure(figsize = (10, 5))
plt.plot(x_axis_fast, all_times_fast, marker='s', linestyle='--', color='r')
plt.xlabel("All integers from 0 to 35")
plt.ylabel("Execution times (secs)")
plt.title("The execution times for each fibonnaci number up to 35 using memoization")
plt.grid(True)
plt.savefig("ex1.6.2.jpg", dpi=300, bbox_inches='tight')
plt.show()
plt.close()

x_axis_slow = list(range(35))
plt.figure(figsize = (10, 5))
plt.plot(x_axis_slow, all_times_slow, marker='s', linestyle='-', color="g")
plt.xlabel("All integers from 0 to 35")
plt.ylabel("Execution times (secs)")
plt.title("The execution times for each fibonnaci number up to 35 not using memoization")
plt.grid(True)
plt.savefig("ex1.6.1.jpg", dpi=300, bbox_inches='tight')
plt.show()
plt.close()



