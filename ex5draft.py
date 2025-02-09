import timeit
from numpy import random
import matplotlib.pyplot as plt

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
            lin_time += timeit.timeit(setup = time_setup, stmt = "linear_search(rand_array, x)", number = 10, globals = {"linear_search": linear_search, "rand_array": rand_array, "x": x, "num": num})
            bin_time += timeit.timeit(setup = time_setup, stmt = "binary_search(rand_array, x)", number = 100, globals = {"binary_search": binary_search, "rand_array": rand_array, "x": x, "num": num})
        lin_time_list.append(lin_time/1000)
        bin_time_list.append(bin_time/1000)

    plt.subplot(1, 2, 1)
    plt.plot(element_list, lin_time_list)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Linear Search")
    scipy.optimize.curve_fit()
    plt.subplot(1, 2, 2)
    plt.plot(element_list, bin_time_list)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Binary Search")
    scipy.optimize.curve_fit()
    plt.show()

if __name__ == "__main__":
    main()

"""
Linear search was fitted by a linear function, and binary search was fitted by a logarithmic function.

"""
