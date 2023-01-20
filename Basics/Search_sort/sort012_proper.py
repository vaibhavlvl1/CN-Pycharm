def sort012(A, n):
    i = 0
    next_zero = 0
    temp = 0
    next_two = len(A)-1

    while i <= next_two:
        if A[i] == 0:
            temp = A[next_zero]
            A[next_zero] = A[i]
            A[i] = temp
            next_zero += 1
            i = i+1

        elif A[i] == 2:
            temp = A[next_two]
            A[next_two] = A[i]
            A[i] = temp
            next_two -= 1
        else:
            i = i+1

    return A


t = int(input())

while t != 0:

    n = int(input())
    A = [int(x) for x in input().split()]
    x = sort012(A, n)
    for ele in x:
        print(ele, end=" ")

    print()

    t = t - 1