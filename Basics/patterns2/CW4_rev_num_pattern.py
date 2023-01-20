"""
to print the following
1
21
321
4321
"""

n = int(input())

i = 1

while(i<=n):
    h = i
    j = 1
    while(j<=i):
        print(h,end="")
        h = h-1
        j = j+1
    print()
    i = i+1

