""" Start of functions we created"""

# In place quicksort implementation
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

#Multi-pivot quicksort methods
def dual_pivot_quicksort(L):
    copy = dual_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_copy(L):
    if len(L) < 2:
        return L

    if L[0] > L[-1]:
        swap(L, 0, -1)

    pivot1 = L[0]
    pivot2 = L[-1]
    left, middle, right = [], [], []

    for num in L[1:-1]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            middle.append(num)

    return dual_copy(left) + [pivot1] + dual_copy(middle) + [pivot2] + dual_copy(right)

def tri_pivot_quicksort(L):
    copy = tri_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def tri_copy(L):
    if len(L) < 2:
        return L
    if len(L) == 2:
        if L[0] > L[1]:
            swap(L, 0, 1)
        return L

    #swap values such that pivot1 <= pivot2 <= pivot3
    swap_for_3(L)

    pivot1 = L[0]
    pivot2 = L[1]
    pivot3 = L[-1]
    left, lmiddle, rmiddle, right = [], [], [], []
    for num in L[2:-1]:
        if num < pivot1:
            left.append(num)
        elif pivot1 <= num < pivot2:
            lmiddle.append(num)
        elif pivot2 <= num < pivot3:
            rmiddle.append(num)
        else:
            right.append(num)

    return (tri_copy(left) + [pivot1] + tri_copy(lmiddle) + [pivot2]
            + tri_copy(rmiddle) + [pivot3] + tri_copy(right))

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def swap_for_3(L):
    if L[0] > L[1]:
        swap(L, 0, 1)
    if L[0] > L[-1]:
        swap(L, 0, -1)
    if L[1] > L[-1]:
        swap(L, 1, -1)

def quad_pivot_quicksort(L):
    copy = quad_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def sort_pivot4(L, i, j, k, l):
    a = [i, j, k, l]
    a.sort()
    L[0], L[1], L[-2], L[-1] = a[0], a[1], a[2], a[3]

def quad_copy(L):
    if len(L) < 2:
        return L
    if len(L) == 2:
        if L[0] > L[1]:
            swap(L, 0, 1)
        return L
    if len(L) == 3:
        swap_for_3(L)
        return L

    sort_pivot4(L, L[0], L[1], L[-2], L[-1])
    pivot1 = L[0]
    pivot2 = L[1]
    pivot3 = L[-2]
    pivot4 = L[-1]

    l, ll, m, rr, r = [], [], [], [], []
    for num in L[2:-2]:
        if num < pivot1:
            l.append(num)
        elif pivot1 <= num < pivot2:
            ll.append(num)
        elif pivot2 <= num < pivot3:
            m.append(num)
        elif pivot3 <= num < pivot4:
            rr.append(num)
        else:
            r.append(num)

    return (quad_copy(l) + [pivot1] + quad_copy(ll) + [pivot2] + quad_copy(m) + [pivot3]
            + quad_copy(rr) + [pivot4] + quad_copy(r))

# Implementation of Insertion Sort
def insertion_sort(L):
    for i in range(1,len(L)):
    
        # Value to compare others compare against
        currentvalue = L[i]
        p1 = i
        
        #Swap previous values which are smaller
        while p1 >= 1 and L[p1-1] > currentvalue:
            L[p1] = L[p1-1]
            p1 -= 1
        
        # Swap end as it has not been taken care of yet
        L[p1] = currentvalue

# Final sort Implementation
def finalSort(L):
    # Call quicksort_helper if list has more than 15 elements
    # Call insertion_sort if list has between 2 and 15 elements
    # List is already sorted if less than 2 elements
    if len(L) > 15:
        quicksort_helper(L,0,len(L)-1)
    elif len(L) > 1:
        insertion_sort(L)

''' End of functions we created'''