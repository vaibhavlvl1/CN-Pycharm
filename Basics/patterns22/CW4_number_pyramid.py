"""
to print following pattern
   1
  232
 34543
4567654

"""


n = int(input())

i = 1
x=2
while(i<=n):

    spaces=1
    while(spaces<=n-i):
        print(" ",end="")
        spaces=spaces+1
    d=i
    j=1
    while(j<=i):
        print(d,end="")
        j+=1
        d+=1

    j=1


    x= 2*i-2
    while(j<=i-1):
        print(x,end="")
        x-=1
        j +=1






    print()
    i +=1
