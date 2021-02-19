""" Start of functions we created"""

# Merge Function (mergesort_bottom(L) helper)


def merge_bottom(L, start, mid, end):

    # Initalize lists to 0
    l_list = L[start:mid+1]
    r_list = L[mid+1:end+1]

    # Lenths of the list to merge
    l_len = len(l_list)
    r_len = len(r_list)

    # Two pointers to keep track of location in both subarrays
    i, j = 0, 0

    # Construct sorted subarray
    while i < l_len and j < r_len:

        # Take element from left list if it is greater
        if l_list[i] > r_list[j]:
            L[start] = r_list[j]
            j += 1

        # Take element from right list if it is greater
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

    # Length of subarray
    length = len(L)

    # Length of subarrays to merge
    subarray_length = 1

    while subarray_length < length:

        # Iterate to find bounds for subarrays
        for i in range(0, length - 1, 2*subarray_length):
            start = i
            mid = i + subarray_length - 1
            end = min(i + 2 * subarray_length - 1, length - 1)

            # Only merge if valid bounds
            if start < length and mid < length and end < length:
                merge_bottom(L, start, mid, end)

        # Subarray length increases exponentianally (2^n)
        subarray_length *= 2


# Three-way mergesort
def mergesort_three(L):
    if len(L) <= 1:
        return
    # Mid points for divide
    mid1 = len(L)//3
    mid2 = mid1*2
    left, mid, right = L[:mid1], L[mid1:mid2], L[mid2:]
    # When length of array is 2
    if len(L) <= 2:
        left, mid, right = L[:1], [], L[1:]

    # Mergesort core
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    temp = merge_three(left, mid, right)

    # Copy sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, mid, right):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(mid) or k < len(right):
        # When 2 arrays are positioned and only one array is left
        if i >= len(left) and j >= len(mid):
            L.append(right[k])
            k += 1
        elif i >= len(left) and k >= len(right):
            L.append(mid[j])
            j += 1
        elif j >= len(mid) and k >= len(right):
            L.append(left[i])
            i += 1
        # When 1 array is positioned
        elif i >= len(left):
            if mid[j] <= right[k]:
                L.append(mid[j])
                j += 1
            else:
                L.append(right[k])
                k += 1
        elif j >= len(mid):
            if left[i] <= right[k]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[k])
                k += 1
        elif k >= len(right):
            if mid[j] <= left[i]:
                L.append(mid[j])
                j += 1
            else:
                L.append(left[i])
                i += 1
        # When no array is fully positioned yet
        else:
            if left[i] <= mid[j]:
                if left[i] <= right[k]:
                    L.append(left[i])
                    i += 1
                else:
                    L.append(right[k])
                    k += 1
            else:
                if mid[j] <= right[k]:
                    L.append(mid[j])
                    j += 1
                else:
                    L.append(right[k])
                    k += 1
    return L


''' End of functions we created'''
