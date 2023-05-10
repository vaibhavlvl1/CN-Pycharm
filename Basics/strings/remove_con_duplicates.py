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



"""
def rem_con_dup(s):
    res = ""
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            continue
        else:
            res+=s[i-1]
            
    res+=s[-1]
    return res
"""