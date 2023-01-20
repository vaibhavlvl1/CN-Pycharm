"""
to print the following pattern

1
22
333
4444

"""

n = int(input())

i = 1
while(i<=n):
    j = 1

    while(j<=i):
        h = i
        print(h, end="")

        j= j+1

    print()
    i = i+1
