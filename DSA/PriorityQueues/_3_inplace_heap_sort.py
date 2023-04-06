"""
 Inplace Heap Sort
Send Feedback
Given an integer array of size N. Sort this array (in decreasing order)
using heap sort.
Note: Space complexity should be O(1).
Input Format:

The first line of input contains an integer, that denotes the value of
the size of the array or N.
The following line contains N space separated integers,
that denote the value of the elements of the array.

Output Format :

The first and only line of output contains array elements after sorting.
The elements of the array in the output are separated by single space.

Constraints :

1 <= n <= 10^6
Time Limit: 1 sec

Sample Input 1:

6
2 6 8 5 4 3

Sample Output 1:

8 6 5 4 3 2


"""

# by min heap we get smallest ele on zeroth index
# but we swap it to the end and perform heapify on rest of n-1 array
# we again get min from that array and we swap it with n-1th ele
# and so on . finally we get smallest elements from r to left
# that is why we get descend sorted array (due to swapping) by using
# min heap


# if we use max heap , we get ascend sorted array

"""
for desc sorted array
"""


def max_heapify(arr, n, i):
    largest = i

    left_child = largest * 2 + 1
    right_child = largest * 2 + 2

    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

    return


"""
for ascd sorted array
"""


def min_heapify(arr, n, i):
    smallest = i
    left_child = smallest * 2 + 1
    right_child = smallest * 2 + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[smallest] > arr[right_child]:
        smallest = right_child

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)





n = input()
arr = [int(ele) for ele in input().split()]
heapsort(arr)
for ele in arr[::-1]:
    print(ele, end=' ')