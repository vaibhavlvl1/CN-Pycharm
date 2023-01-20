def sort012(A, n):
    H = []
    x = A.count(0)
    y = A.count(1)
    z = A.count(2)

    for i in range(x):
        H.append(0)
    for i in range(y):
        H.append(1)
    for i in range(z):
        H.append(2)

    return H


t = int(input())

while t != 0:

    n = int(input())
    A = [int(x) for x in input().split()]
    x = sort012(A, n)
    for ele in x:
        print(ele, end=" ")

    print()

    t = t - 1