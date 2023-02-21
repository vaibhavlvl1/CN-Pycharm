from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesAtDepth(root, k):
    if root is None:
        return

    if k == 0:
        print(root.data)
        return
    nodesAtDepth(root.left, k - 1)
    nodesAtDepth(root.right, k - 1)


def nodesAtDistanceK(root, node, k):
    if node is None:
        return -1
    if root is None:
        return -1

    if root.data == node:
        nodesAtDepth(root, k)
        return 0

    leftLength = nodesAtDistanceK(root.left, node, k)
    if leftLength != -1:
        if leftLength + 1 == k:
            print(root.data)
        else:
            nodesAtDepth(root.right, k - leftLength - 2)
        return leftLength + 1
    rightLength = nodesAtDistanceK(root.right, node, k)
    if rightLength != -1:
        if rightLength + 1 == k:
            print(root.data)
        else:
            nodesAtDepth(root.left, k - rightLength - 2)
            return rightLength + 1

    return -1


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
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)