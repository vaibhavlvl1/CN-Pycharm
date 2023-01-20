"""
to print following pattern
1
11
202
3003
"""






n = int(input())

i = 1
x =1
print("1")



while(i<=n-1):
    print(x, end="")
    j = 1

    while(j<=i-1):

        print("0",end="")

        j=j+1

    print(x, end="")

    print()

    i= i+1
    x= x+1



