# first reach end then print
# 1 to n
def nat_num(n):
    if n==0:
        return
    nat_num(n-1)
    print(n)
    return

nat_num(10)


# n - to 1 print
def n_to_1(n):
    if n==0:
        return
    print(n)
    n_to_1(n-1)
    return

n_to_1(10)