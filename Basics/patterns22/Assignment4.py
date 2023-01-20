'''
to print the following pattern

*
 * *
   * * *
     * * * *
   * * *
 * *
*
'''


N = int(input())

n1=(N+1)/2
n2 = n1-1

i=1
while(i<=n1):
    spaces=1
    while(spaces<=i-1):
        print(" ",end="")
        spaces=spaces+1

    stars = 1
    while(stars<=i):
        print("* ",end="")
        stars=stars+1

    i=i+1
    print()

i =1
while(i<=n2):

    spaces=1
    while(spaces<=n2-i):
        print(" ",end="")
        spaces +=1

    stars = 1
    while(stars<=n2-i+1):
        print("* ",end="")

        stars +=1

    print()
    i = i+1


