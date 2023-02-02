"""
PRINT not RETURN
"""
from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print


#recursion
def print_rev_ll(head):
    if head is None:
        return
    print_rev_ll(head.next)
    print(head.data,end=" ")





# linear

def rev_linked_list(head):
    curr = head
    prev = None

    while curr is not None:
        save = curr.next
        curr.next = prev
        prev = curr
        curr = save
    return prev

head = linked_list_input()
linked_list_print(rev_linked_list(head))