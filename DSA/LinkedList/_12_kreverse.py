from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse3(head):
    if head is None:
        return
    curr = head
    prev = None
    while curr is not None:
        save = curr.next
        curr.next = prev
        prev = curr
        curr = save
    return prev, head


def kreverse(head, k):
    if k == 0 or k == 1:
        return head
    if head is None:
        return head
    c = 0
    curr = head
    while curr is not None:
        if c == k:
            break
        c = c + 1
        prev = curr
        curr = curr.next
    prev.next = None

    newhead, newtail = reverse3(head)

    newtail.next = kreverse(curr, k)

    return newhead


# Taking Input Using Fast I/O
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
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kreverse(head, k)
    printLinkedList(newHead)

    t -= 1