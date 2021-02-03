import timeit
import random

# Copy Method
def copy_time(list_to_copy):
    duplicate = list_to_copy.copy()


# List which increases in size every iteration
sample_list = []

# Loop to time list with increasing number of integers
def copy_test():
    for _ in range(5000):

        start_time = timeit.default_timer()
        copy_time(sample_list)
        end_time = timeit.default_timer()
        print(end_time - start_time)

        sample_list.append(random.randrange(1000000))


def append_test():
    for i in range(1000000):
        start = timeit.default_timer()
        sample_list.append(random.randint(1, 1000000))
        end = timeit.default_timer()
        with open("values.txt", "a") as f:
            f.write(f"{end - start}\n")


def append_test2():
    for i in range(100000):
        a = [random.randint(0, 100000) for _ in range(100)]
        start = timeit.default_timer()
        sample_list.append(a)
        end = timeit.default_timer()
        with open("values.txt", "a") as f:
            f.write(f"{end - start}\n")


append_test2()


# Lookups

# Initialize list with random values
lookup_list = random.sample(range(1, 1000001), 1000000)

# Lookup time method
def lookup_time(list_to_lookup, index):
    list_to_lookup[index]


# Open file for data
f = open("lookup.txt", "w")

for i in range(len(lookup_list)):

    start_time = timeit.default_timer()
    lookup_time(lookup_list, i)
    end_time = timeit.default_timer()
    f.write("{1:d}\t{0:.10f}\r".format(end_time - start_time, i))
f.close()


# Lookup redesign
lookup_list_redesign = random.sample(range(1, 1000001), 1)


f = open("lookup_redesign.txt", "w")

for i in range(1000000):

    start_time = timeit.default_timer()
    lookup_time(lookup_list_redesign, i)
    end_time = timeit.default_timer()
    f.write("{1:d}\t{0:.10f}\r".format(end_time - start_time, i))
    lookup_list_redesign.append(random.randrange(1000000))
f.close()
