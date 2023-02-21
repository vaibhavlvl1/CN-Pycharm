from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def reverseStack(s1, s2):
    if len(s1) <= 1:
        return

    while len(s1) != 1:
        x = s1.pop()
        s2.append(x)

    lastElement = s1.pop()

    while (len(s2) != 0):
        x1 = s2.pop()
        s1.append(x1)

    reverseStack(s1, s2)
    s1.append(lastElement)


'''-------------- Utility Functions --------------'''


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def takeInput():
    size = int(stdin.readline().strip())
    inputStack = list()

    if size == 0:
        return inputStack

    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")