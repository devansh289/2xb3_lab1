import random
import math
import timeit

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def quicksort_random_test():
    for i in range(10000):
        f = open('quicksort.txt', 'a')

        test_list = create_random_list(i)

        start_time = timeit.default_timer()
        my_quicksort(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

        f.close()

    open('quicksort.txt', 'a')

def quicksort_nearly_sorted_test():
    for i in range(10000):
        f = open('quicksort.txt', 'a')

        test_list = create_near_sorted_list(i, 0.1)

        start_time = timeit.default_timer()
        my_quicksort(test_list)
        end_time = timeit.default_timer()

        f.write(str(end_time - start_time) + '\n')

        f.close()

    open('quicksort.txt', 'a')

def small_list_test():
    f = open('quicksort.txt', 'a')
    for i in range(20):
        values = []
        for _ in range(10000):
        
            test_list = create_random_list(i)

            start_time = timeit.default_timer()
            my_quicksort(test_list)
            end_time = timeit.default_timer()

            values.append(end_time - start_time)

        f.write(str(sum(values)/len(values)) + '\n')
        values = []
    f.close()