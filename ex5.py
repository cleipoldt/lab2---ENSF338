import timeit
from numpy import random
import matplotlib.pyplot as plt
import scipy
import numpy as np

def linear_search(array, elem):
    pos = 0
    for item in array:
        if item == elem:
            return pos
        pos += 1
    return -1

def binary_search(array, elem):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right)/2)
        if array[mid] == elem:
            return mid
        elif array[mid] > elem:
            right = mid - 1
        elif array[mid] < elem:
            left = mid + 1
    return -1

def lin_func(x, a, b):
    return a * x + b
def log_func(x, a, b):
    return a * np.log(x) + b

def main():
    element_list = [1000, 2000, 4000, 8000, 16000]
    lin_time_list = []
    bin_time_list = []

    time_setup = "from numpy import random"
    
    for num in element_list:
        print(f"Measuring performance of search for {num} elements...")
        rand_array = sorted(random.randint(num, size = (num)))
        lin_time = 0
        bin_time = 0
        for i in range(1000):
            x = random.randint(num)
            lin_time += timeit.timeit(setup = time_setup, stmt = "linear_search(rand_array, x)", number = 100, globals = {"linear_search": linear_search, "rand_array": rand_array, "x": x, "num": num})
            bin_time += timeit.timeit(setup = time_setup, stmt = "binary_search(rand_array, x)", number = 100, globals = {"binary_search": binary_search, "rand_array": rand_array, "x": x, "num": num})
        lin_time_list.append(lin_time/1000)
        bin_time_list.append(bin_time/1000)

    #how to get equation of each fitline?
    #linear fitline is wrong, in the slides he mentioned that "we already know how to fit a linear function from class"?
    slope, intercept = np.polyfit(element_list, lin_time_list, 1)
    #plt.scatter(element_list, lin_time_list)
    linevalues = [slope * x + intercept for x in element_list]
    coeffs, covar = scipy.optimize.curve_fit(lin_func, element_list, bin_time_list)
    a_fit, b_fit = coeffs
    x_fit = np.linspace(min(element_list), max(element_list))
    y_fit = lin_func(x_fit, slope, slope)
    plt.subplot(1, 2, 1)
    plt.plot(element_list, linevalues, 'r')
    #plt.plot(element_list, lin_time_list)
    plt.plot(x_fit, y_fit, label = 'Linear Fit')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Linear Search")
    print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))

    coeffs, covar = scipy.optimize.curve_fit(log_func, element_list, bin_time_list)
    a_fit, b_fit = coeffs
    x_fit = np.linspace(min(element_list), max(element_list))
    y_fit = log_func(x_fit, a_fit, b_fit)
    plt.subplot(1, 2, 2)
    plt.plot(element_list, bin_time_list)
    plt.plot(x_fit, y_fit, label = 'Logarithmic Fit', color = 'green')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Binary Search")
    plt.show()

if __name__ == "__main__":
    main()

"""
4.  (1) Linear search was fitted by a linear function, and binary search was fitted by a logarithmic function.
        The parameters of the linear function are: x_fit, slope and slope where x_fit is an array of evenly spaced 
        values between the minimum and maximum of element_list. The parameters of the logarithmic function are: x_fit, 
        a_fit and b_fit where x_fit is the same as in the linear function and the a_fit and b_fit are coefficients of 
        the logarithmic function.
    (2) Yes, the results are what we expected. Since the time complexity for linear search is O(n), we expected the 
        graph to be linear. The time complexity for binary search is O(log n) so we expected the graph to be 
        logarithmic.

"""
