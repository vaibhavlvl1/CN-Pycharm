def sum_of(n):
    if n<10:
        return n

    return n%10 + sum_of(n//10)

print(sum_of(12345))