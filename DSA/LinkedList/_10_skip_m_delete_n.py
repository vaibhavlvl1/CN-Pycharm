"""
 Delete every N nodes
Send Feedback
You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.
Note :

No need to print the list, it has already been taken care. Only return the new head to the list.

Input format :

The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.

 Remember/Consider :

While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element

Output format :

For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.

Constraints :

1 <= t <= 10^2
0 <= P <= 10^5
Where P is the size of the singly linked list.
0 <= M <= 10^5
0 <= N <= 10^5

Time Limit: 1sec

Sample Input 1 :

1
1 2 3 4 5 6 7 8 -1
2 2

Sample Output 1 :

1 2 5 6

Sample Input 2 :

2
10 20 30 40 50 60 -1
0 1
1 2 3 4 5 6 7 8 -1
2 3

Sample Output 2 :

1 2 6 7

Explanation of Sample Input 2 :

For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.


"""
from PACKAGES.LINKED_LIST import linked_list_print,linked_list_input

def skip_m_delete_n(m,n,head):
    if head is None:
        return
    if m==0:
        return
    if n==0:
        return head
    curr = head
    prev = None
    c=0
    while curr is not None:
        if c==m:
            break
        prev = curr
        curr = curr.next
        c=c+1
    d=0
    while curr is not None:
        if d==n:
            break
        curr = curr.next
        d=d+1
    prev.next = skip_m_delete_n(m,n,curr)
    return head



head = linked_list_input()
skip_m_delete_n(2,2,head)
linked_list_print(head)