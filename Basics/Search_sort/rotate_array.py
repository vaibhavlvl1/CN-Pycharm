def rotate(A, N):
    temp = []
    for i in range(N):
        temp.append(A[i])
    A = A[N:]

    for ele in temp:
        A.append(ele)
    return A


t = int(input())

for t in range(t):
    n = int(input())
    if n == 0:
        break

    A = [int(x) for x in input().split()]

    N = int(input())

    x = rotate(A, N)

    for ele in x:
        print(ele, end=" ")

    print()