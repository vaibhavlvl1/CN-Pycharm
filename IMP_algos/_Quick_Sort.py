"""
Quick_Sort
"""

def partition(arr, si, ei):
    pivot = arr[si]
    count = 0

    for i in range(si+1, ei+1):
        if arr[i] < pivot:
            count = count+1

    pivot_index = count+si

    arr[si], arr[pivot_index] = arr[pivot_index],arr[si]

    i = si
    j = len(arr)-1

    while i<j:
        if arr[i] < pivot:
            i = i+1
        elif arr[j] > pivot:
            j = j-1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return pivot_index







arr = [4,1,3,2,5,9,7]

def quicksort(arr, si, ei):
    if si>=ei:
        return

    pivot_index = partition(arr,si,ei)
    quicksort(arr,si,pivot_index-1)
    quicksort(arr,pivot_index+1,ei)

    return arr


arr = [4,1,3,2,5,9,7]
li = quicksort(arr,0,len(arr)-1)
print(li)


