import timeit
from lab3, sorts import *

#Calculate time for quicksort_inplace with random values
def quicksort_random_test():
    f = open('quicksort.txt', 'a')

    for i in range(10000):
    
        test_list = create_random_list(i)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

    f.close()

#Calculate time for my_quicksort with almost sorted values
def quicksort_nearly_sorted_test():
    f = open('quicksort.txt', 'a')
    for i in range(10000):
        
        test_list = create_near_sorted_list(i, 0.1)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

    f.close()

#Calculate time for quicksort_inplace with small lists
def quicksort_small_list_test():
    f = open('quicksort.txt', 'a')

    for i in range(20):
        values = []
        for _ in range(10000):
        
            test_list = create_random_list(i)

            start_time = timeit.default_timer()
            quicksort_inplace(test_list)
            end_time = timeit.default_timer()

            values.append(end_time - start_time)

        f.write(str(sum(values)/len(values)) + '\n')
        values = []
    f.close()

#Calculate time for insertion_sort with small lists
def insertion_small_list_test():
    f = open('quicksort.txt', 'a')

    for i in range(20):
        values = []
        for _ in range(10000):
        
            test_list = create_random_list(i)

            start_time = timeit.default_timer()
            insertion_sort(test_list)
            end_time = timeit.default_timer()

            values.append(end_time - start_time)

        f.write(str(sum(values)/len(values)) + '\n')
        values = []
    f.close()
