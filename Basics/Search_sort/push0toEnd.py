def filter(A):
    i, k = 0, 0
    for i in range(n):
        if A[i] != 0:
            A[k] = A[i]
            k = k + 1
    while (k < n):
        A[k] = 0
        k = k + 1

    return A


t = int(input())

for t in range(t):

    n = int(input())

    A = [int(x) for x in input().split()]

    h = filter(A)
    # print(h)
    for ele in h:
        print(ele, end=" ")
    print()