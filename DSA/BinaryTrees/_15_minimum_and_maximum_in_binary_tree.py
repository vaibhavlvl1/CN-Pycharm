from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Representation of the Pair Class
class Pair:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum


def getMax(root):
    if root is None:
        return -1
    maxi = root.data

    leftMax = getMax(root.left)
    rightMax = getMax(root.right)
    NetMax = max(leftMax, rightMax)

    if maxi < NetMax:
        maxi = NetMax

    return maxi


def getMin(root):
    if root is None:
        return 100

    mini = root.data
    leftMin = getMin(root.left)
    rightMin = getMin(root.right)
    NetMin = min(leftMin, rightMin)

    if mini > NetMin:
        mini = NetMin

    return mini


def getMinAndMax(root):
    mini = getMin(root)
    maxi = getMax(root)

    p = Pair(mini, maxi)

    return p


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

pair = getMinAndMax(root)
print(str(str(pair.minimum) + " " + str(pair.maximum)))



"""
combined method

def min_max_binary_tree(root):
    if root is None:
        return 9999999,-1
    
    mini = root.data
    maxi = root.data
        
    left_min,left_max = min_max_binary_tree(root.left)
    right_min,right_max = min_max_binary_tree(root.right)
    net_mini = min(left_min,right_min)
    net_maxi = max(left_max,right_max)
    
    if mini > net_mini:
        mini = net_mini
    if maxi<net_maxi:
        maxi = net_maxi
    
    return mini,maxi
"""