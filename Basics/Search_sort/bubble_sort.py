def bubble_sort(A):
    for i in range(n):
        temp =0
        for j in range(i+1):
            if A[i] < A[j]:
                temp = A[j]
                A[j]=A[i]
                A[i]=temp


    return A


t = int(input())

for t in range(t):

    n = int(input())
    if n == 0:
        print("")
        break

    A = [int(x) for x in input().split()]

    d = bubble_sort(A)

    for ele in d:
        print(ele, end=' ')

    print()