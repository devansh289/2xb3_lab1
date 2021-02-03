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
    else: