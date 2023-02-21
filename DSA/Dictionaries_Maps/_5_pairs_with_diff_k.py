"""
 Pairs with difference K
Send Feedback
You are given with an array of integers and an integer K. You have to find and print the count of all such pairs which have difference K.
Note: Take absolute difference between the elements of the array.
Input Format:

The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol n.
The following line contains n space separated integers, that denote the value of the elements of the array.
The following line contains an integer, that denotes the value of K.

Output format :

The first and only line of output contains count of all such pairs which have an absolute difference of K.

Constraints :

0 <= n <= 10^4
Time Limit: 1 sec

Sample Input 1 :

4
5 1 2 4
3

Sample Output 1 :

2

Sample Input 2 :

4
4 4 4 4
0

Sample Output 2 :

6


"""


def printPairDiffK(l, k):
    if len(l) == 0:
        return
    d = {}
    pairs = 0

    for ele in l:
        if ele + k in d:
            pairs += d[ele + k]
        if k != 0 and ele - k in d:
            pairs += d[ele - k]
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1

    return pairs


# Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
k = int(input())
print(printPairDiffK(l, k))