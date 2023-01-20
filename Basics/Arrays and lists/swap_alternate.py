def swap_alternate(li, n):
    for i in range(0, n - 1, 2):
        li[i], li[i + 1] = li[i + 1], li[i]

    for ele in li:
        print(ele, end=' ')


t = int(input())

while (t != 0):

    n = int(input())
    if n == 0:
        break
    li = [int(x) for x in input().split()]
    swap_alternate(li, n)
    print()
    t -= 1