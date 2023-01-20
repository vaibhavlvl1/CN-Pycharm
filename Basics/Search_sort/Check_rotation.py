def check_rot(arr, n):
    min = arr[0]
    k = 0
    for i in range(0, n):

        if (min > arr[i]):
            min = arr[i]
            k = i

    return (k)


t = int(input())

while (t != 0):

    n = int(input())
    if n == 0:
        print('0')
        break
    arr = [int(x) for x in input().split()]

    print(check_rot(arr, n))

    t = t - 1