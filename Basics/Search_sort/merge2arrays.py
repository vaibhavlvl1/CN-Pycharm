from sys import stdin


def merge(arr1, n, arr2, m):
    i, j = 0, 0
    res_array = []
    while (i < n and j < m):

        if arr1[i] < arr2[j]:
            res_array.append(arr1[i])
            i = i + 1

        else:  # a1[i]>=a2[j]
            res_array.append(arr2[j])
            j = j + 1

    while (i < n):
        res_array.append(arr1[i])
        i = i + 1
    while (j < m):
        res_array.append(arr2[j])
        j = j + 1
    return res_array


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1