import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    if not lst:
        return None
    l = len(lst)
    mid = (l - 1) // 2
    root = BinaryTreeNode(lst[mid])
    # leftSubTree = lst[:mid]
    # rightSubTree = lst[mid+1:]

    root.left = constructBST(lst[:mid])
    root.right = constructBST(lst[mid + 1:])

    return root


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)