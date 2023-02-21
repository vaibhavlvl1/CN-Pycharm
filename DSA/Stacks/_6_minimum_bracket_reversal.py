class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:
            return "stack Empty Bro"
        x = self.data.pop()
        return x

    def top(self):
        if len(self.data) == 0:
            return "Stack Empty Bro"
        return self.data[-1]

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def size(self):
        return len(self.data)

    def printStack(self):
        for i in range(self.size()):
            print(self.data[i], end=" ")

    def pushToBegin(self, pos, ele):
        self.data.insert(pos, ele)


def balanceBrackets(st):
    if (len(st) % 2) != 0:
        return -1
    s = []

    for ele in st:
        if ele == "{":
            s.append(ele)
        elif ele == "}" and len(s) != 0 and s[-1] == "{":
            s.pop()
        else:
            s.append(ele)

    if (len(s) % 2) != 0:
        return -1
    count = 0
    while len(s) > 0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count = count + 2
        else:
            count += 1

    return count


expression = input()

s = balanceBrackets(expression)

print(s)
