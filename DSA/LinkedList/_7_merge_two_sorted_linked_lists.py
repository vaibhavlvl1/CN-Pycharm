"""
 Code : Merge two sorted LL
Send Feedback
You have been given two sorted(in ascending order) singly linked lists of integers.
Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order) and return the new head to the list.
Note :

Try solving this in O(1) auxiliary space.

No need to print the list, it has already been taken care.

Input format :

The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the first sorted singly linked list separated by a single space.

The second line of the input contains the elements of the second sorted singly linked list separated by a single space.

Remember/Consider :

While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output :

For each test case/query, print the resulting sorted singly linked list, separated by a single space.

Output for every test case will be printed in a seperate line.

Constraints :

1 <= t = 10^2
0 <= N <= 10 ^ 4
0 <= M <= 10 ^ 4
Where N and M denote the sizes of the singly linked lists.

Time Limit: 1sec

Sample Input 1 :

1
2 5 8 12 -1
3 6 9 -1

Sample Output 1 :

2 3 5 6 8 9 12

Sample Input 2 :

2
2 5 8 12 -1
3 6 9 -1
10 40 60 60 80 -1
10 20 30 40 50 60 90 100 -1

Sample Output 2 :

2 3 5 6 8 9 12
10 10 20 30 40 40 50 60 60 60 80 90 100


"""

from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print


def merge_two_sorted_ll(lisa,mona):
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


head1 = linked_list_input()
head2 = linked_list_input()

new_head = merge_two_sorted_ll(head1,head2)
linked_list_print(new_head)