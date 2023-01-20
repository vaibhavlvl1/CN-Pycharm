"""
to print following pattern
*000*000*
0*00*00*0
00*0*0*00
000***000
"""


n= int(input(""))

i = 1

while(i<=n):

    j=1

    while(j<=n):

        if i==j:
            print("*",end="")
        else:
            print("0",end='')
        j=j+1


    print("*",end="")
    j=1
    while(j<=n):

        if j==(n-i+1):
            print("*",end='')

        else:
            print("0",end='')
        j=j+1

    print()
    i = i+1