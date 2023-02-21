"""
 Return Keypad
Send Feedback
Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
Note : The order of strings are not important.
Input Format :

Integer n

Output Format :

All possible strings in different lines

Constraints :
1 <= n <= 10^6
Sample Input:

23

Sample Output:

ad
ae
af
bd
be
bf
cd
ce
cf


"""


def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"


def keypad(n):
    if n == 0:
        return [""]

    smallInteger = n // 10
    lastDigit = n % 10

    smallOutput = keypad(smallInteger)
    optionsForLastDigit = getString(lastDigit)

    output = []

    for s in smallOutput:
        for c in optionsForLastDigit:
            output.append(s + c)

    return output


n = int(input())
ans = keypad(n)
for s in ans:
    print(s)