import timeit
from lab4 import *
from sorts import *
import sys

# Performance comparison of 2-way vs 3-way mergesort


def mergesort_test():
    f = open('mergesort_two.txt', 'a')
    for n in range(500):
        values = []
        for _ in range(100):
            test_list = create_random_list(n+1)

            start_time = timeit.default_timer()
            mergesort(test_list)
            end_time = timeit.default_timer()

            values.append(end_time - start_time)
        f.write(str(n+1) + '\t' + str(sum(values)/len(values)) + '\r')
    f.close()


def mergesort_three_test():
    f = open('mergesort_three.txt', 'a')
    for n in range(500):
        values = []
        for _ in range(100):

            test_list = create_random_list(n+1)

            start_time = timeit.default_timer()
            mergesort_three(test_list)
            end_time = timeit.default_timer()

            values.append(end_time - start_time)

        f.write(str(n+1) + '\t' + str(sum(values)/len(values)) + '\r')
    f.close()
