from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print,\
    linked_list_midpoint,linked_list_length

"""
 Code : Merge Sort
Send Feedback
 Given a singly linked list of integers, sort it using 'Merge Sort.'
Note :

No need to print the list, it has already been taken care. Only return the new head to the list.

Input format :

The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.

Remember/Consider :

While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output format :

For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.

Constraints :

1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec

Sample Input 1 :

1
10 9 8 7 6 5 4 3 -1

Sample Output 1 :

 3 4 5 6 7 8 9 10 

 Sample Input 2 :

2
-1
10 -5 9 90 5 67 1 89 -1

Sample Output 2 :

-5 1 5 9 10 67 89 90 


"""

def merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = linked_list_midpoint(head)
    head2 = mid.next
    mid.next = None

    head1 = merge_sort(head)
    head2 = merge_sort(head2)

    return merge(head1,head2)


def merge(mona,lisa):
    if mona is None:
        return lisa
    elif lisa is None:
        return mona
    if lisa.data<mona.data:
        head = lisa
        tail = lisa
        lisa = lisa.next
    else:
        head = mona
        tail = mona
        mona = mona.next
    while lisa is not None and mona is not None:
        if lisa.data<mona.data:
            tail.next = lisa
            tail = tail.next
            lisa = lisa.next
        else:
            tail.next = mona
            tail = tail.next
            mona = mona.next
    while lisa is not None:
        tail.next = lisa
        tail = tail.next
        lisa = lisa.next
    while mona is not None:
        tail.next = mona
        tail = tail.next
        mona = mona.next
    return head


heh = linked_list_input()
linked_list_print(merge_sort(heh))

