"""
to print following pattern
1
11
121
1221

"""


n = int(input())

i =  1

print("1")

while(i<=n-1):

    j = 1
    print("1",end="")
    while(j<=i-1):
        print("2",end="")

        j = j+1

    print("1")

    i = i+1