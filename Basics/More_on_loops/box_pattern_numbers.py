# print the pattern

"""
n = 5
1 2 3 4 5
11 12 13 14 15
21 22 23 24 25
16 17 18 19 20
6 7 8 9 10
"""


## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())

n = N + (N - 1)

n1 = (n + 1) / 2
n1 = int(n1)
n2 = n1 - 1
l = N
k = N
h = N
f = n2
p = n2 - 1
for i in range(1, n1 + 1):

    x = N
    for j in range(i):
        print(x, end="")
        x = x - 1

    for j in range(n1 - i):
        print(l, end="")

    l = l - 1

    for j in range(n1 - i):
        print(k, end="")

    k = k - 1
    p = 1
    for j in range(i - 1):
        print(h + p, end="")
        p = p + 1
    h = h - 1

    print()

for i in range(1, n2 + 1):

    p = 0
    for j in range(n2 - i + 1):
        print(N - p, end="")

        p = p + 1

    for j in range(i):
        print(i + 1, end="")

    for j in range(i - 1):
        print(i + 1, end="")

    p = 0
    for j in range(n2 - i + 1):
        print(i + 1 + p, end="")

        p = p + 1

    print()