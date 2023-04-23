"""
Minimum bracket Reversal
Send Feedback
For a given expression in the form of a string, find the minimum number of brackets that can be
 reversed in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.
Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced.
Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first
 opening bracket and hence will not be able to make the expression balanced and the output will be -1.
Input Format :
The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
The only line of output will print the number of reversals required to balance the whole expression.
Prints -1, otherwise.
Note:
You don't have to print anything. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1sec
Sample Input 1:
{{{
Sample Output 1:
-1
Sample Input 2:
{{{{}}
Sample Output 2:
1
"""

class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:
            return "stack Empty Bro"
        x = self.data.pop()
        return x

    def top(self):
        if len(self.data) == 0:
            return "Stack Empty Bro"
        return self.data[-1]

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def size(self):
        return len(self.data)

    def printStack(self):
        for i in range(self.size()):
            print(self.data[i], end=" ")

    def pushToBegin(self, pos, ele):
        self.data.insert(pos, ele)


def balanceBrackets(st):
    if (len(st) % 2) != 0:
        return -1
    s = []

    for ele in st:
        if ele == "{":
            s.append(ele)
        elif ele == "}" and len(s) != 0 and s[-1] == "{":
            s.pop()
        else:
            s.append(ele)

    if (len(s) % 2) != 0:
        return -1
    count = 0
    while len(s) > 0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count = count + 2
        else:
            count += 1

    return count


expression = input()

s = balanceBrackets(expression)

print(s)
