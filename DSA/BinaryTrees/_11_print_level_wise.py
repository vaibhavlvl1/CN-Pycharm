from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    q = queue.Queue()

    q.put(root)
    if q.empty():
        return None

    while q.empty() != True:
        Node = q.get()

        print(Node.data, end=":")
        if Node.left is not None:
            print("L:" + str(Node.left.data), end=",")
        else:
            print("L:" + "-1", end=",")
        if Node.right is not None:
            print("R:" + str(Node.right.data))
        else:
            print("R:" + "-1", end="")
            print()

        if Node.left is not None:
            q.put(Node.left)
        if Node.right is not None:
            q.put(Node.right)


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


# Main
root = takeInput()
printLevelWise(root)