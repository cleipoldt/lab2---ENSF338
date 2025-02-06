import timeit
from numpy import random

def main():
    # list containing number of elements for each iteration
    element_list = [1000, 2000, 4000, 8000, 16000, 32000]
    # list to be filled by timeit timing each iteraiton and putting into list
    time_list = []

    for num in element_list:
        # code to be looped 
        x = random.randint(num)
        # unsure about the specifications of the elements themselves?
        rand_array = sorted(random.randint(num, size = (num)))
        # find x in rand_array using searches

        #time it
        total_time = timeit.timeit(setup = org_setup, stmt = org_code, number = 1000)
        time_list.append(total_time)

if __name__ == "__main__":
    main()


