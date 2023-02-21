from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getRoot(li):
    return li.pop(0)


def getIndex(m, li):
    for index, ele in enumerate(li):
        if ele == m:
            return index


def debug(root, root_index, inOrder, preOrder):
    print("root  ", root)
    print("root_index  ", root_index)
    leftTreeLength = len(inOrder[0:root_index])
    rightTreeLength = len(inOrder[root_index + 1:])
    leftSubTree = preOrder[0:leftTreeLength]
    rightSubTree = preOrder[leftTreeLength:]

    print("leftTreeLenght   ", inOrder[0:root_index], "  ", leftTreeLength)
    print("rightTreeLength   ", inOrder[root_index + 1:], "   ", rightTreeLength)
    print("leftSubTree  ", leftSubTree)
    print("rightSubTree  ", rightSubTree)


def buildTree(preOrder, inOrder, n):
    if len(preOrder) == 0:
        return None
    rootdata = getRoot(preOrder)  # in preoder
    root = BinaryTreeNode(rootdata)

    root_index = getIndex(rootdata, inOrder)

    leftTreeLength = len(inOrder[0:root_index])
    rightTreeLength = len(inOrder[root_index + 1:])
    leftInorder = inOrder[0:root_index]
    rightInorder = inOrder[root_index + 1:]

    # debug(root,root_index,inOrder,preOrder)

    leftSubTree = preOrder[0:leftTreeLength]
    rightSubTree = preOrder[leftTreeLength:]

    root.left = buildTree(leftSubTree, leftInorder, n)
    root.right = buildTree(rightSubTree, rightInorder, n)

    return root


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# # Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)