from PACKAGES.BINARYTREE import tree_input


def get_sum(root):
    if root is None:
        return 0

    left_sum = get_sum(root.left)
    right_sum = get_sum(root.right)
    total_sum = root.data+left_sum+right_sum

    return total_sum




# Main
root = tree_input()
print(get_sum(root))