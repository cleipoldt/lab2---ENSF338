'''
Questions:
1. What is a profiler, and what does it do? 
2. How does profiling differs from benchmarking? 
3. Use a profiler to measure execution time of the program (skip
function definitions) 
4. Discuss a sample output. Where does execution time go? 

Answers:
1.  A profiler is a tool to help analyze program performance. It does this by collecting data on different aspects of 
    a program such as the amount of time it takes for a function to run and how many times the functions are called to 
    find which sections of the program are slowest. Profilers can also help with optimizing memory and CPU usage as 
    they identify where the code is taking up too much memory. This is helpful as it allows us to focus our attention 
    on the proper functions that need further optimization. 

2.  Profiling differs from benchmarking as profiling provides a more in-depth analysis of code execution by focusing 
    on the performance of functions in the program, revealing which functions need further improvement. Benchmarking 
    is different as it measures the performance of the entire code without diving deeper into the little details. So 
    benchmarking can tell you which program performs better while profiling tells you which functions to focus on to 
    improve a program's performance.

4.  A sample output is: . The execution time 
'''

import timeit
import cProfile 

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

cProfile.run('test_function()')
cProfile.run('third_function()')

def main():
    return 0

if __name__ == "__main__":
    main()