def sel_sort(li, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if li[j] < li[min]:
                min = j
        li[min], li[i] = li[i], li[min]

    return li


t = int(input())

for t in range(t):

    n = int(input())
    if n == 0:
        print("")
        break

    li = [int(x) for x in input().split()]

    x = sel_sort(li, n)
    for ele in x:
        print(ele, end=' ')

    print()
