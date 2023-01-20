"""
to print the following patterns

  *
 ***
*****
 ***
  *

"""

N = int(input())

n1= (N+1)/2

i = 1

while(i<=n1):

    spaces=1
    while(spaces<=n1-i):
        print(" ",end="")
        spaces+=1

    stars=1
    while(stars<=2*i-1):
        print("*",end='')

        stars+=1
    print()
    i = i+1


n2 = n1-1

i=2

while(i!=0):

    spaces=1
    while(spaces<=n2-i+1):
        print(" ",end="")
        spaces+=1

    stars=1
    while(stars<=2*i-1):
        print("*",end="")
        stars+=1
    print()
    i -=1
