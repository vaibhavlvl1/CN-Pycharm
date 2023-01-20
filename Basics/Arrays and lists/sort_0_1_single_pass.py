def segregate0and1(arr):

    left, right = 0,len(arr)-1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    return arr


t = int(input())

while (t != 0):

    k = int(input())

    if k == 0:
        print("")
        break

    arr = [int(x) for x in input().split()]

    arr_size = len(arr)

    h = (segregate0and1(arr))

    for ele in h:
        print(ele, end=" ")

    t = t - 1
    print()