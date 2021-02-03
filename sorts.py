import timeit, random, math

''' Start of Functions provided with the lab '''
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

''' End of functions provided with the lab '''



''' Start of functions we created'''

def quicksort_helper(L,start,end):
    #The pivot element is chosen to be the last one in the list
    pivot_element = L[end]
    
    # Pointer to keep track of value greater than pivot
    p1 = start
    
    #Check to see if array has atleast two element
    if start < end:
        
        for i in range(start,end+1):
            # If current value <= pivot then swap
            if L[i]<=pivot_element:
                L[p1], L[i] = L[i], L[p1]
                
                # Move pointer to next element
                if i != end:
                    p1+=1
        
        #Sort the left subarray
        quicksort_helper(L, start, p1-1)
        
        #Sort the right subarray
        quicksort_helper(L, p1+1, end)
    return L
   
def quicksort_inplace(L):
    
    # Only call quicksort_helper if list has atleast 2 elements
    if len(L)>1:
        quicksort_helper(L,0,len(L)-1)

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 



''' End of functions we created'''