# finally my own solution

def pair_sum(li, K):
    res = []
    i = 0
    numpairs = 0

    for i in range(n):

        for j in range(i + 1, n):

            if li[i] + li[j] == K:
                numpairs += 1

    return numpairs


t = int(input())
while (t != 0):
    n = int(input())
    if n == 0:
        print("0")
        break

    li = [int(x) for x in input().split()]

    K = int(input())

    h = pair_sum(li, K)

    print(h)

    t = t - 1
