# IMPLEMENTATION OF LINKED LIST

"""
implementation of linked list to be used as package
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def linked_list_input():
    head = None
    arr = [int(i) for i in input().split()]
    for curr_data in arr:
        if curr_data==-1:
            break
        new_node = Node(curr_data)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next
    return head

def linked_list_print(head):
    while head is not None:
        print(head.data,end="-->")
        head = head.next
    print("None")

def linked_list_length(head):
    temp = head
    c = 0
    while temp is not None:
        c = c+1
        temp = temp.next
    return c

def linked_list_reverse(head):
    """
    By iterative method
    :param head: head of ll
    :return: new_head
    """
    curr = head
    prev = None

    while curr is not None:
        save = curr.next
        curr.next = prev
        prev = curr
        curr = save
    return prev