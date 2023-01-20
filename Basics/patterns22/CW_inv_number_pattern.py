"""
to print following pattern

4444
333
22
1


"""

n = int(input())

i = 4
while(i!=0):

    j=1
    while(j<=i):
        print(i,end="")
        j=j+1

    print()
    i = i-1


"""
another method
n = int(input())

i = i
x=4
while(i<=n):

    j=1
    
    while(j<=n-i+1):
        print(x,end="")
        j=j+1
    x=x-1

    print()
    i = i+1



"""