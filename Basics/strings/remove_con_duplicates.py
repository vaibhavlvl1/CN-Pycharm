def conDupRem(str, n):
    out = ''
    for i in range(n - 1):
        if str[i] != str[i + 1]:
            out = out + str[i]
    out = out + str[n - 1]

    for j in out:
        print(j, end='')


# MAIN
str = input()
conDupRem(str, len(str))