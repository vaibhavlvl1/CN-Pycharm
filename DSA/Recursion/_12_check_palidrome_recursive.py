"""

"""

def pali(str):
    if len(str)==0:
        return ""

    return pali(str[1:])+str[0]

# str = "vaibhav"
# x = pali(str)
# print(x)
# print(str==x)


############################## another ##########################


def palindrome(str):
    if len(str)==0:
        return True
    if str[0] != str[-1]:
        return False
    return palindrome(str[1:-1])
print(palindrome("nursesrun"))
