from sys import stdin
import queue


def checkRedundantBrackets(st):
    s = []

    for ele in st:
        if ele == ")":
            c = 0
            while s.pop() != "(":
                c = c + 1
            if c <= 1:
                return True

        s.append(ele)






