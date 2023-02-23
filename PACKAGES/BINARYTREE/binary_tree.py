# IMPLEMENTATION OF BINARY TREES NODE INPUTS AND TRAVERSALS

"""
implementation of binary tree to be used as package
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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



import queue
def level_wise_input():
    q = queue.Queue()
    root_data = int(input())

    if root_data==-1:
        return None
    root = BinaryTreeNode(root_data)

    q.put(root)

    while not q.empty():
        current_node = q.get()

        print(f"Enter left child of {current_node.data}: ")
        left_child_data = int(input())
        if left_child_data !=-1:
            left_child = BinaryTreeNode(left_child_data)
            q.put(left_child)
            current_node.left = left_child

        print(f"Enter right child of {current_node.data}: ")
        right_child_data = int(input())
        if right_child_data != -1:
            right_child = BinaryTreeNode(right_child_data)
            q.put(right_child)
            current_node.right = right_child
    return root

def print_level_order(root):
    if root is None:
        return None

    print(root.data)
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        curr_node = q.get()
        if curr_node.left is not None:
            print(curr_node.left.data)
            q.put(curr_node.left)
        if curr_node.right is not None:
            print(curr_node.right.data)
            q.put(curr_node.right)