from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 9)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def containsX(tree, X):
    #############################

    if tree.data == X:
        return True

    for child in tree.children:
        if containsX(child, X):
            return True

    return False

    #############################


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main

arr = list(int(x) for x in stdin.readline().strip().split())
x = int(stdin.readline().strip())
tree = createLevelWiseTree(arr)
if containsX(tree, x):
    print('true')
else:
    print('false')