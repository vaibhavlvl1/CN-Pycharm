"""
split ll in half then reverse one part then compare them
"""
from PACKAGES.LINKED_LIST import linked_list_input,\
    linked_list_print,linked_list_length,linked_list_reverse

def midpoint(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next  is not None :
        slow = slow.next
        fast = fast.next.next
    return slow


def palindrome(head):
    if head is None or length(head) == 1:
        return True
    mid = midpoint(head)
    head2 = mid.next
    mid.next = None
    linked_list_print(head)
    linked_list_print(head2)

    rev_head2 = linked_list_reverse(head2)
    linked_list_print(rev_head2)

    while rev_head2 is not None and head is not None:
        if rev_head2.data != head.data:
            return False
        else:
            rev_head2 = rev_head2.next
            head = head.next
    return True


head = linked_list_input()

print(palindrome(head))