from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print

def find_node(head,node_data,c=0):
    if head is None:
        return -1
    if head.data==node_data:
        return c
    return find_node(head.next,node_data,c+1)


head = linked_list_input()
print(find_node(head,4))


