"""
 Return Permutations of a String
Send Feedback
Given a string, find and return all the possible permutations of the input string.
Note : The order of permutations are not important.
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


def perm(string):
    if len(string) == 0:
        return [""]

    output = []

    for i in range(len(string)):
        start = string[i]

        remString = string[:i] + string[i + 1:]

        smalloutput = perm(remString)

        for sub in smalloutput:
            output.append(start + sub)

    return output


s = input()
ans = perm(s)
for i in ans:
    print(i)


