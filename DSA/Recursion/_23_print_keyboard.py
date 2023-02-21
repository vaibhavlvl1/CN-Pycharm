"""
 Print Keypad
Send Feedback
Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
Note : The order of strings are not important. Just print different strings in new lines.
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

val = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}


def printKeypad(n, outputSoFar):
    if n == 0:
        print(outputSoFar)
        return

    smallNumber = n // 10
    lastDigit = n % 10
    optionForLastDigit = val.get(lastDigit)

    for c in optionForLastDigit:
        newOutput = c + outputSoFar
        printKeypad(smallNumber, newOutput)


n = int(input())
printKeypad(n, "")