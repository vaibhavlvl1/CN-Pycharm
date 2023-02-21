from sys import stdin
import queue


def isBalanced(st):
    s = []

    for ele in st:
        if ele == "(":
            s.append(ele)
        elif ele == ")" and len(s) != 0:
            s.pop()
        else:
            s.append(ele)

    if len(s) != 0:
        return False
    return True


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")
