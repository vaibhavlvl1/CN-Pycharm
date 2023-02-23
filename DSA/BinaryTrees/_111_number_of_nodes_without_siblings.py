from PACKAGES.BINARYTREE import tree_input,print_tree_detailed

def num_nodes_without_siblings(root):
    if root.left is None and root.right is None:
        return 1

    if root.left is not None:
        left_side = num_nodes_without_siblings(root.left)
    else:
        left_side = 0
    if root.right is not None:
        right_side = num_nodes_without_siblings(root.right)
    else:
        right_side = 0

    return left_side+right_side

root = tree_input()
print(num_nodes_without_siblings(root))