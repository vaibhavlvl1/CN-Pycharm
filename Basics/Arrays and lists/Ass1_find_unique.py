def find_unique(li):
    result = []
    for i in li:
        if li.count(i) == 1:
            result.append(i)
            return result


t = int(input())

while (t != 0):

    n = int(input())
    li = [int(x) for x in input().split()]

    x = find_unique(li)

    for ele in x:
        print(ele)

    t = t - 1