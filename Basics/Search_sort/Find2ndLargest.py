def sec_larg(A, n):
    if A.count(A[0]) == len(A):
        return -2 ** 31

    l, s = 0, 0

    for i in range(n):
        if l<A[i]:
            s=l
            l=A[i]
        if l>A[i]:
            if s<A[i]:
                s=A[i]







    # print(A)
    return (s)


t = int(input())

for t in range(t):

    n = int(input())
    A = [int(x) for x in input().split()]
    if n <= 1:
        print(-2 ** 31)
        break

    print(sec_larg(A, n))