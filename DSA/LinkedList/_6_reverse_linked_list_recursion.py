from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print

def rev_link_list_recursion(head):
    if head.next is None:
        return head
    smallhead = rev_link_list_recursion(head.next)
    head.next.next = head
    head.next = None
    return smallhead

head = linked_list_input()
new_head = rev_link_list_recursion(head)
linked_list_print(new_head)
