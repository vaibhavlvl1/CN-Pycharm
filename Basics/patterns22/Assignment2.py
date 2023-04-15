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

"""
For LOop

def pat(n):
    for i in range(0,n+1):
        
        for j in range(n):
            if i==j:
                print("x",end=" ")
            else:
                print("0",end = " ")
        print("x",end=" ")        
               
        for j in range(n):
            if n-j-1 == i:
                print("x",end=" ")
            else:
                print("0",end=" ")
        print()
"""