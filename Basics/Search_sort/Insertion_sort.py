def ins_sort(arr):
    for i in range(1, n):
        j = i - 1
        temp = arr[i]
        while (j >= 0 and arr[j] > temp):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr


t = int(input())

for t in range(t):

    n = int(input())

    arr = [int(x) for x in input().split()]

    z = ins_sort(arr)

    for ele in z:
        print(ele, end=" ")

    print()


"""
def ins_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        
        j = i-1
            
        while  j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
"""