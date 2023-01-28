"""
TIME_COMPLEXITY - The time complexity of merge sort is
O(n*Log n) for all cases (best, average and worst).
"""

def merge(a,b,c):
    i = 0
    j = 0
    k = 0

    while i<=len(a)-1 and j<=len(b)-1:
        if a[i]<b[j]:
            c[k]=a[i]
            i = i+1
            k=k+1
        else:
            c[k] = b[j]
            j = j+1
            k = k+1
    while i<=len(a)-1:
        c[k] = a[i]
        i = i+1
        k = k+1
    while j<=len(b)-1:
        c[k] = b[j]
        j = j+1
        k = k+1





def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2

    a = arr[:mid]
    b = arr[mid:]

    merge_sort(a)
    merge_sort(b)
    merge(a,b,arr)


arr = [3,5,2,3,9,6,7,6,1,0]
merge_sort(arr)
print(arr)