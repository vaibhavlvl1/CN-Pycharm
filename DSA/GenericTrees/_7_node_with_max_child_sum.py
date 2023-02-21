from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans


def maxSumNode(tree):
    if tree is None:
        return tree, Sum

    ans = tree
    Sum = tree.data

    for child in tree.children:
        Sum = Sum + child.data

    for child in tree.children:
        tempRoot, tempSum = maxSumNode(child)
        if tempSum > Sum:
            Sum = tempSum
            ans = tempRoot
    return ans, Sum


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
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)