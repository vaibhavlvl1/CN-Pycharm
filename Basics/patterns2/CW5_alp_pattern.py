"""
to print the following pattern
A
BC
CDE
DEFG

"""

n = int(input())

i = 1

x = ord("A")

while(i<=n):

    j = 1

    while(j<=i):

        print(chr(x+j-1),end="")

        j  = j+1
    x = x+1
    print()
    i=i+1