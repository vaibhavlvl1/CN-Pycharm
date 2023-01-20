def cbs(li, k):
    lb = 0
    ub = len(li) - 1

    while lb <= ub:
        m = (lb + ub) // 2

        if k == li[m]:
            return m

        elif k < li[m]:
            ub = m - 1
        else:
            lb = m + 1

    return -1


n = int(input())

li = [int(x) for x in input().split()]

t = int(input())
if n == 0:
    print("-1")

else:

    for t in range(0, t):
        k = int(input())
        j = cbs(li, k)
        print(j)