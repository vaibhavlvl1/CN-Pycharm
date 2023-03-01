"""
 Path Sum Root to Leaf
Send Feedback
For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the node data along the path is equal to K.
Example:

alt txt

If you see in the above-depicted picture of Binary Tree, we see that there are a total of two paths, starting from the root and ending at the leaves which sum up to a value of K = 13.

The paths are:
a. 2 3 4 4
b. 2 3 8

One thing to note here is, there is another path in the right sub-tree in reference to the root, which sums up to 13 but since it doesn't end at the leaf, we discard it.
The path is: 2 9 2(not a leaf)

 Input Format:

The first line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

The second line of input contains an integer value K.

Output Format:

Lines equal to the total number of paths will be printed. All the node data in every path will be printed in a linear fashion taken in the order they appear from top to down bottom in the tree. A single space will separate them all.

Constriants:

1 <= N <= 10^5
0 <= K <= 10^8
Where N is the total number of nodes in the binary tree.

Time Limit: 1 second

Sample Input 1:

2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
13

 Sample Output 1:

2 3 4 4
2 3 8

Sample Input 2:

5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
13

 Sample Output 2:

5 6 2
5 7 1


"""

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    if root is not None:
        if root.right is None and root.left is None:
            return True
        else:
            return False
    return False


def rootToLeafPathsSumToK(root, k, path=""):
    if k is None or k <= 0:
        return
    if isLeaf(root) == True and k == root.data:
        path += str(root.data)
        print(path)
        return
    if root is None:
        return

    path += str(root.data) + " "

    rootToLeafPathsSumToK(root.left, k - root.data, path)
    rootToLeafPathsSumToK(root.right, k - root.data, path)


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k)