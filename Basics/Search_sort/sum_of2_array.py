def sum2array(a1, a2):
    result = []

    k = max(n1, n2)
    ans = 0

    # for i in range(k):
    # result.append(0)
    carry = 0
    i = n1 - 1
    j = n2 - 1
    while k >= 0:
        d = carry

        if i >= 0:
            d += a1[i]
        if j >= 0:
            d += a2[j]
        carry = d // 10
        d = d % 10

        result.append(d)

        i = i - 1
        j = j - 1
        k = k - 1

    if carry > 0:
        print(carry, end=" ")

    result.reverse()

    for x in result:
        print(x, end=' ')


t = int(input())

while (t != 0):
    n1 = int(input())
    if n1 > 0:
        a1 = [int(x) for x in input().split()]
    n2 = int(input())
    if n2 >= 0:
        a2 = [int(x) for x in input().split()]
    if n1 == 0 and n2 == 0:
        print("0")
        break

    sum2array(a1, a2)

    t = t - 1