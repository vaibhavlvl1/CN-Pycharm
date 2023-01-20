"""
to print following pattern
E
DE
CDE
BCDE
ABCDE

"""

n = int(input())

i = 1

while(i<=n):
    f_memba = ord("E")
    j = 1

    while(j<=i):

        print(chr(f_memba-i+j),end="")
        j = j+1

    #f_memba -=1

    print()
    i = i+1
