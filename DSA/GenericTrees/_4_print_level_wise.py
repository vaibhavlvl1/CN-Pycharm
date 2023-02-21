import sys
import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def printLevelWiseTree(tree):
    q = queue.Queue()

    q.put(tree)

    while q.empty() == False:
        node = q.get()
        print(node.data, end=":")
        if len(node.children) != 0:
            print(node.children[0].data, end="")
            q.put(node.children[0])
        for i in range(1, len(node.children)):
            if node.children[i].data is not None:
                print(",", end="")
            print(node.children[i].data, end="")
            q.put(node.children[i])
        print()


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
sys.setrecursionlimit(10 ** 6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)