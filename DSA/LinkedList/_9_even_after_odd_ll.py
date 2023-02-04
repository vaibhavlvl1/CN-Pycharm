"""
 Even after Odd LinkedList
Send Feedback
For a given singly linked list of integers, arrange the elements such
that all the even numbers are placed after the odd numbers.
The relative order of the odd and even terms should remain unchanged.
Note :

No need to print the list, it has already been taken care. Only return the new head to the list.

Input format:

The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

 Remember/Consider :

While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output format:

For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.

Constraints :

1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec

Sample Input 1 :

1
1 4 5 2 -1

Sample Output 1 :

1 5 4 2

Sample Input 2 :

2
1 11 3 6 8 0 9 -1
10 20 30 40 -1

Sample Output 2 :

1 11 3 9 6 8 0
10 20 30 40


"""

from PACKAGES.LINKED_LIST import linked_list_input,linked_list_print

def is_even(int):
    return int % 2 == 0
def even_odd(head):
    odd_head =None
    even_head = None

    while head is not None:
        if is_even(head.data):
            if not even_head:
                even_head= head
                even_tail = head
                head = head.next
            else:
                even_tail.next = head
                even_tail = even_tail.next
                head = head.next
        else:
            if not odd_head:
                odd_head = head
                odd_tail = head
                head = head.next
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
                head = head.next

    if even_head is None:
        return odd_head
    elif odd_head is None:
        even_tail.next = None
        return even_head
    else:
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head


head = linked_list_input()
linked_list_print(even_odd(head))

