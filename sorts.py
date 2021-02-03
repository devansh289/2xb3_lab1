def partition(L, start, end):
    
    index = start
    pivot = L[index]

    while start < end:
        while start < len(L) and L[start] <= pivot:
            start+=1

        while L[end] > pivot:
            end-=1

        if start < end:
            L[start], L[end] = L[end], L[start]

    L[index], L[end] = L[end], L[index]

    return end
    
def quick_sort(L, start, end):
    if start < end:
        partition_index = partition(L, start, end)
        quick_sort(L, start, partition_index-1)
        quick_sort(L, partition_index+1, end)

