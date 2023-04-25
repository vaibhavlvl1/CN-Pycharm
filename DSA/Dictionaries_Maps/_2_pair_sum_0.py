"""
 Pair Sum To 0
Send Feedback
Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
Note: Array A can contain duplicate elements as well.
Input format:

The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.

Output format :

The first and only line of output contains the count of pair of elements in the array which sum up to 0.

Constraints :

0 <= N <= 10^4
Time Limit: 1 sec

Sample Input 1:

5
2 1 -2 2 3

Sample Output 1:

2


"""

from sys import stdin


def pairSum0(l, n):
    d = {}
    NoPairs = 0

    for ele in l:
        if 0 - ele in d:
            NoPairs += d[0 - ele]
            print(0-ele,ele)

        if ele in d:
            d[ele] += 1
        elif ele not in d:
            d[ele] = 1

    return NoPairs


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n





def pair_sum(arr, k):
    d = {}
    c = 0
    for ele in arr:
        if 0 - ele in d:
            print(0 - ele, ele)
            c += d[0 - ele]
        if ele in d:
            d[ele] += 1
        elif ele not in d:
            d[ele] = 1

    return c

arr, n = takeInput()
print(pair_sum(arr, 0))