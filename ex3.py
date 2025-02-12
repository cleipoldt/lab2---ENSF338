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
    benchmarking can tell you which program performs better while profiling tells you which functions you need to work 
    on to improve a program's performance.

4.  A sample output is: 

         71 function calls (26 primitive calls) in 4.151 seconds

    Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    4.151    4.151 <string>:1(<module>)
    55/10    0.000    0.000    0.000    0.000 ex3.py:28(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:35(test_function)
        1    3.158    3.158    3.158    3.158 ex3.py:41(third_function)
        1    0.993    0.993    4.151    4.151 ex3.py:45(main)
        1    0.000    0.000    4.151    4.151 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
    In the sample output above we can see that there were 71 function calls with 26 of them being primitive that took 
    a total of 4.151 seconds to complete. The ncalls column shows the number of calls each parts of the program 
    required to make. The execution time goes in the cumtime column.
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

def main():
    test_function()
    third_function()
    return 0

if __name__ == "__main__":
    main()
    cProfile.run('main()')