"""
 Print Permutations of a String
Send Feedback
Given a string, find and print all the possible permutations of the input string.
Note : The order of permutations are not important. Just print them in different lines.
Sample Input :

abc

Sample Output :

abc
acb
bac
bca
cab
cba


"""


def perm(string, output):
    if len(string) == 0:
        print(output)
        return

    for i in range(len(string)):
        start = string[i]
        remaining = string[:i] + string[i + 1:]
        perm(remaining, output + start)


s = input()
perm(s, "")
