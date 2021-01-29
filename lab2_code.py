import timeit
import random

#Copy Method
def copy_time(list_to_copy):
    duplicate = list_to_copy.copy()

# List which increases in size every iteration
sample_list = []

# Loop to time list with increasing number of integers
for _ in range(500):

    start_time = timeit.default_timer()
    copy_time(sample_list)
    end_time = timeit.default_timer()
    print(end_time - start_time)

    sample_list.append(random.randrange(1000000))

