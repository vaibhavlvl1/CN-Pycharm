from sys import stdin


class Stack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        # self.count = 0

    def getSize(self):
        return len(self.s2)

    def isEmpty(self):
        return self.getSize() == 0

    def enqueue(self, data):
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        self.s2.append(data)

        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

    def dequeue(self):
        if len(self.s2) == 0:
            return -1
        return self.s2.pop(0)

    def front(self):
        if len(self.s2) == 0:
            return -1
        return self.s2[0]


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.enqueue(data)

    elif choice == 2:
        print(stack.dequeue())

    elif choice == 3:
        print(stack.front())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1