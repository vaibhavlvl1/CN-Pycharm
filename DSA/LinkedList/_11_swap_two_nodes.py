from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    temp = head  # avoiding head to become none # it doesnt matter anyway
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def swapNodes(head, i, j):
    if i == j:
        return head
    if head is None:
        return
    size = length(head)

    if i > j:  # so that i is always small
        temp = i
        i = j
        j = temp

    # case 1
    if i == 0 and 1 < j < size - 1:
        curr = head
        prev = None
        c = 0
        while curr is not None:
            if c == j:
                break
            c = c + 1
            prev = curr
            curr = curr.next
        save = curr.next
        save2 = head.next
        prev.next = head
        head.next = save
        curr.next = save2
        return curr

    # case 2

    if i == 0 and j == size - 1:
        if size == 2:
            newtail = head
            newhead = head.next
            newhead.next = newtail
            newtail.next = None
            return newhead
        c = 0
        curr = head
        prev = None
        while curr is not None:
            if c == j:
                break
            c = c + 1
            prev = curr
            curr = curr.next
        save = head.next
        curr.next = save
        head.next = None
        prev.next = head

        return curr

    # case 3
    if 0 < i < j and j == size - 1 and j - i != 1:
        c = 0
        prev = None
        curr = head
        c = 0
        while curr is not None:
            if c == i:
                break
            prev = curr
            curr = curr.next
            c = c + 1
        save = curr.next
        tail = head
        prevTail = None
        while tail.next is not None:
            prevTail = tail
            tail = tail.next

        prev.next = tail
        tail.next = save
        prevTail.next = curr
        curr.next = None

        return head

    # case 4

    if 0 < i < j and i < j < size - 1 and j - i != 1:
        c = 0
        curr1 = head
        prev1 = None

        while curr1 is not None:
            if c == i:
                break
            c = c + 1
            prev1 = curr1
            curr1 = curr1.next

        save1 = curr1.next
        c = 0
        curr2 = head
        prev2 = None

        while curr2 is not None:
            if c == j:
                break
            c = c + 1
            prev2 = curr2
            curr2 = curr2.next
        save2 = curr2.next

        prev1.next = curr2
        curr2.next = save1
        prev2.next = curr1
        curr1.next = save2

        return head

    # case 5

    if j - i == 1:
        # sub-case 1
        if i == 0:
            newHead = head.next
            save = head.next.next
            head.next = save
            newHead.next = head

            return newHead
        # sub-case 2
        if j == size - 1:
            curr = head
            prev = None
            while curr.next.next is not None:
                prev = curr
                curr = curr.next
            save = curr.next
            prev.next = save
            save.next = curr
            curr.next = None
            return head

        else:  # sub-case 3
            c = 0
            prev = None
            curr = head
            while curr is not None:
                if c == i:
                    break
                prev = curr
                c = c + 1
                curr = curr.next
            save1 = curr.next
            save2 = curr.next.next
            prev.next = save1
            save1.next = curr
            curr.next = save2
            return head


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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1