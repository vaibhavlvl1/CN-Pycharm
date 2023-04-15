# Binary Pattern

"""
n = 4
1111
000
11
1
"""

n = int(input())

for i in range(n):

    for j in range(n - i):

        if i % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()


# using while loop

# n = int(input())
#
# i = 0
# while i<=n:
#     j = n-i
#     while j!=0:
#         if i%2==0:
#             print("1",end="")
#         else:
#             print("0",end="")
#         j = j-1
#     print()
#     i = i+1