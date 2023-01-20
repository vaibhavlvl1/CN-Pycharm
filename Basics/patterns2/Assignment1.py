"""
to print following pattern on screen
1
11
111
1111
"""


n = int(input(""))

i = 1

while(i<=n):

    j = 1

    while(j<=i):

        print("1",end="")

        j=j+1


    print()
    i = i+1