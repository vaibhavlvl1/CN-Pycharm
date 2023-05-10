import queue


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lcaOfThreeNodes(root, node1, node2, node3):
    if root is None:
        return None

    if root.data == node1 or root.data == node2 or root.data == node3:
        return root

    left_lca = lcaOfThreeNodes(root.left, node1, node2, node3)
    right_lca = lcaOfThreeNodes(root.right, node1, node2, node3)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


# Building the tree.
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length <= 0 or levelorder[0] == -1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


t = int(input())
while t > 0:
    arr = [int(i) for i in input().split()][:3]
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(lcaOfThreeNodes(root, arr[0], arr[1], arr[2]).data)
    t = t - 1


