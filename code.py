import timeit
from lab3 import *
from sorts import *
import sys

# Calculate time for quicksort_inplace with random values


def quicksort_random_test():
    f = open('quicksort.txt', 'a')

    for i in range(10000):

        test_list = create_random_list(i)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

    f.close()

# Calculate time for my_quicksort with almost sorted values


def quicksort_nearly_sorted_test():
    f = open('quicksort.txt', 'a')
    for i in range(10000):

        test_list = create_near_sorted_list(i, 0.1)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

    f.close()

# Calculate time for quicksort_inplace with small lists


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

# Calculate time for insertion_sort with small lists


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


# Worst case analysis of quicksort
sys.setrecursionlimit(10**6)

def quicksort_multi(quicksort, runs):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        quicksort
        end = timeit.default_timer()
        total += end - start
    return total / runs

def quick_multi_pivot_test():
    f = open("quick_multipivot_data.txt", "a")
    for _ in range(0, 100000, 100):
        a = create_random_list(_)
        f.write(str(_) + "\t" + str(quicksort_multi(my_quicksort(a), 1)) + "\t" +
                str(quicksort_multi(dual_pivot_quicksort(a), 1)) + "\t" +
                str(quicksort_multi(tri_pivot_quicksort(a), 1)) + "\t" +
                str(quicksort_multi(quad_pivot_quicksort(a), 1)) + "\n")
    f.close()

quick_multi_pivot_test()

def quicksort_worst_case_test():
    f = open('worstcase.txt', 'a')

    for n in range(10000):
        test_list = create_random_list(n)
        test_list.sort(reverse=True)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(n) + '\t' + str(end_time - start_time) + '\r')
    f.close()


def quicksort_avg_case_test():
    f = open('worstcase.txt', 'a')

    for n in range(3500):
        test_list = create_random_list(n)

        start_time = timeit.default_timer()
        quicksort_inplace(test_list)
        end_time = timeit.default_timer()

        f.write(str(n) + '\t' + str(end_time - start_time) + '\r')
    f.close()


def time_test(sort_function, L):
    start_time = timeit.default_timer()
    sort_function(L)
    end_time = timeit.default_timer()
    return end_time - start_time


def near_sort_analysis():
    f = open('worstcase.txt', 'a')

    for n in range(1000):

        quick_sort_time = time_test(
            quicksort_inplace, create_near_sorted_list(1000, (n+1)/1000))
        merge_sort_time = time_test(
            merge_sort, create_near_sorted_list(1000, (n+1)/1000))
        tim_sort_time = time_test(
            sorted, create_near_sorted_list(1000, (n+1)/1000))
        insertion_sort_time = time_test(
            insertion_sort, create_near_sorted_list(1000, (n+1)/1000))

        f.write(str((n+1)/1000) + '\t' + str(quick_sort_time) + '\t' + str(merge_sort_time) + '\t' + str(tim_sort_time) +
                '\t' + str(insertion_sort_time) + '\r')
    f.close()

