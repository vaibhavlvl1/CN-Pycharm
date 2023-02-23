from PACKAGES.BINARYTREE import tree_input,print_tree_detailed

def remove_leaf_nodes(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None

    root.left = remove_leaf_nodes(root.left)
    root.right = remove_leaf_nodes(root.right)

    return root




root = tree_input()
remove_leaf_nodes(root)
print_tree_detailed(root)
