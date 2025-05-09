"""
 Print Subsets of Array
Send Feedback
Given an integer array (of length n), find and print all the subsets of input array.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
Note : The order of subsets are not important. Just print the subsets in different lines.
Input format :

Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)

Constraints :
1 <= n <= 15
Sample Input:

3
15 20 12

Sample Output:

[] (this just represents an empty array, don't worry about the square brackets)
12
20
20 12
15
15 12
15 20
15 20 12


"""


def subset(arr, output):
    if len(arr) == 0:
        print(output)
        return

    subset(arr[1:], output)

    newoutput = output + "" + str(arr[0]) + " "

    subset(arr[1:], newoutput)


n = int(input())

arr = [int(x) for x in input().split()]

subset(arr, "")