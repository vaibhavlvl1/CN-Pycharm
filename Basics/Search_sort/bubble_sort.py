def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


t = int(input())

for t in range(t):

    n = int(input())
    if n == 0:
        print("")
        break

    A = [int(x) for x in input().split()]

    bubble_sort(A)

    print(A)