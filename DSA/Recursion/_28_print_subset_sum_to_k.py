"""
 Print Subset Sum to K
Send Feedback
Given an array A and an integer K, print all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
Note : The order of subsets are not important. Just print them in different lines.
Input format :

Line 1 : Size of input array
Line 2 : Array elements separated by space
Line 3 : K

Sample Input:

9
5 12 3 17 1 18 15 3 17
6

Sample Output:

3 3
5 1



"""


def printsubsetk(arr, k, lst):
    n = len(arr)
    if n == 0:
        return
    if n == 1:
        if arr[0] == k:
            print(k, *lst)
            return

    printsubsetk(arr[:-1], k, lst)
    printsubsetk(arr[:-1], k - arr[-1], [arr[-1]] + lst)

    if arr[-1] == k:
        print(k, *lst)


n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())
printsubsetk(arr, k, [])


