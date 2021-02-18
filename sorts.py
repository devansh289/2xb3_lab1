""" Start of functions we created"""

# Merge Function (mergesort_bottom(L) helper)
def merge_bottom(L, start, mid, end): 
    
    # Initalize lists to 0
    l_list = L[start:mid+1]
    r_list = L[mid+1:end+1]
    
    #Lenths of the list to merge
    l_len = len(l_list)
    r_len = len(r_list)
    
    # Two pointers to keep track of location in both subarrays
    i, j = 0, 0
    
    #Construct sorted subarray
    while i < l_len and j < r_len: 
        
        #Take element from left list if it is greater
        if l_list[i] > r_list[j]: 
            L[start] = r_list[j] 
            j += 1
            
        #Take element from right list if it is greater
        else: 
            L[start] = l_list[i] 
            i += 1
        start += 1
 
    # Check if either list has left over elements
    while i < l_len: 
        L[start] = l_list[i] 
        i += 1
        start += 1
 
    while j < r_len: 
        L[start] = r_list[j] 
        j += 1
        start += 1

# Call this function to sort
def mergesort_bottom(L):
    
    #Length of subarray
    length = len(L)
    
    #Length of subarrays to merge
    subarray_length = 1
    
    while subarray_length < length:
 
        #Iterate to find bounds for subarrays
        for i in range(0, length - 1, 2*subarray_length):
            start = i
            mid = i + subarray_length - 1
            end = min(i + 2 * subarray_length - 1, length - 1)
            
            # Only merge if valid bounds
            if start < length and mid < length and end < length:
                merge_bottom(L, start, mid, end)
 
        # Subarray length increases exponentianally (2^n)
        subarray_length *= 2
 

''' End of functions we created'''
