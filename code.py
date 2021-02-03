import sorts

def quicksort_random_test():
    for i in range(10000):
        f = open('quicksort.txt', 'a')

        test_list = sorts.create_random_list(i, 0.1)

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


