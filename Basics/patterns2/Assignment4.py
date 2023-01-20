"""
to print following pattern
1234
123
12
1
"""


n = int(input(""))

i = 1

while(i<=n):

    j = 1
    p = 1
    while(j<=n-i+1):
        print(p,end="")

        p = p+1
        j= j+1

    print()
    i = i+1