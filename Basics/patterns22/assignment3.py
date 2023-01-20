'''
to print the following pattern

   1
  212
 32123
4321234
'''

n= int(input())

i = 1
while(i<=n):

    spaces=1
    while(spaces<=n-i):
        print(" ",end="")

        spaces +=1


    d=i
    j=1
    while(j<=i):
        print(d,end="")

        d=d-1
        j = j+1

    l=1
    m=2
    while(l<=i-1):


        print(m,end="")

        l=l+1
        m=m+1

    print()
    i=i+1

