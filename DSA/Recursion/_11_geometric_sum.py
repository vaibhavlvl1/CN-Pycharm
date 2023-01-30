"""
Given k, find the geometric sum i.e.

1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)

answer shouldf be in 5 digits after decimal
"""


def geometric_sum(k):
    if k==0:
        return 1

    return 1/2**(k)+ geometric_sum(k-1)


print("%.5f" % geometric_sum(3))

