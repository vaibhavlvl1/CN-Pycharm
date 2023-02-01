from PACKAGES.LINKED_LIST import print_linked_list,linked_list_input


def find_node(head,node_data,pos = 0):
    while head is not None:
        if head.data == node_data:
            return pos
        head = head.next
        pos = pos+1
    return -1


# head = linked_list_input()
# print(find_node(head,5))
