# IMPLEMENTATION OF BINARY TREES NODE INPUTS AND TRAVERSALS

"""
implementation of binary tree to be used as package
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def tree_input():
    root_data = int(input())
    if root_data == -1:
        return
    root = BinaryTreeNode(root_data)
    root.left = tree_input()
    root.right = tree_input()
    return root

def print_tree(root):
    if root is None:
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)


def print_tree_detailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L-", root.left.data,end="")
    if root.right is not None:
        print("R-", root.right.data)
    print()
    print_tree_detailed(root.left)
    print_tree_detailed(root.right)

def preorder_traversal(root):
    if root is None:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)