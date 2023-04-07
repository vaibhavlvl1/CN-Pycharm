from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.count = 0
        self.tail = None

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            self.count += 1
        # return self.head

    def dequeue(self):
        if self.count == 0:
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.count -= 1
            return data

    def front(self):
        if self.count == 0:
            return -1
        return self.head.data




# main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2:
        print(queue.dequeue())

    elif choice == 3:
        print(queue.front())

    elif choice == 4:
        print(queue.getSize())

    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1