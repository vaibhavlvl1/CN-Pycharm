"""
Print the nth Fib number
"""

def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

#print(fib(0))

# print all fib num
def fib2(n):
    for i in range(n+1):
        print(fib(i))




fib2(8)