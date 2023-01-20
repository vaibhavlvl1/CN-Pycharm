n = int(input('How many rows'))
m = int(input('How many columns'))

#list input

li = [[int(x) for x in input().split()] for i in range (n)]

def largest_sum_column(a) :

    index = 0
    max = 0
    for j in range(m):
        sum = 0
        for i in range(n):

            sum = sum + a[i][j]
            if max < sum:
                max = sum
                index = j
    return index,sum

x = largest_sum_column(li)

print(x)