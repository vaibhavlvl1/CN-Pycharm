##Print Number Pyramid

"""
n = 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
"""


def numPyramid(n):
    # First Half
    for i in range(1, n + 1):
        # first half spaces
        for j in range(i - 1):
            print(".", end="")
        # first half numbers
        m = i
        for j in range(n - i, -1, -1):
            print(m, end="")
            m = m + 1
        print()
    # second half
    n1 = n - 1
    for i in range(n1):
        # spaces
        for j in range(n1 - i - 1):
            print(".", end="")
        # numbers
        x = n - i - 1
        for j in range(n - x + 1):
            print(x, end="")
            x = x + 1

        print()