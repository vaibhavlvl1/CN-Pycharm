t = int(input())


# from itertools import combinations

def findTriplets(arr, n, sum):
    res = []
    numpairs = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] +
                        arr[k] == sum):
                    numpairs += 1
    return numpairs


while (t != 0):
    n = int(input())
    if n == 0:
        print("0")
        break

    li = [int(x) for x in input().split()]

    K = int(input())

    h = findTriplets(li, n, K)

    print(h)
    t = t - 1
