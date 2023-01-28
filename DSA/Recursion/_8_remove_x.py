"""
remove x from the string
"""


def rem(str,x):
    if len(str)==0:
        return ""

    if str[0]==x:
        return rem(str[1:],x)
    return str[0]+rem(str[1:],x)


str = "vaibhav"
x = 'a'
print(rem(str,x))