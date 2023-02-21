from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    c = 0
    while head is not None:
        head = head.next
        c = c + 1
    return c


def bubbleSort(head):
    n = length(head)

    for i in range(n - 1):
        prev = None
        curr = head
        for j in range(n - i - 1):

            if curr.data <= curr.next.data:
                prev = curr
                curr = curr.next
            else:
                if prev is None:
                    new = curr.next
                    head = head.next
                    curr.next = new.next
                    new.next = curr

                    prev = new
                else:
                    new = curr.next
                    prev.next = new
                    # head = head.next
                    curr.next = new.next
                    new.next = curr
                    prev = new

    return head


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)