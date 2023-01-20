"""
to print the following pattern

    *
   ***
  *****
 *******

"""


n = int(input(""))

i = 1

while(i<=n):
    spaces=1
    while(spaces<=n-i):
        print(" ",end="")
        spaces=spaces+1


    stars=1
    while(stars<=i):
        print("*",end="")

        stars +=1


    stars=1
    while(stars<=i-1):
        print("*",end="")

        stars +=1

    print()
    i=i+1