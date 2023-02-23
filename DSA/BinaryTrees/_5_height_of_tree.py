from PACKAGES.BINARYTREE import tree_input


def height(root):
    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)



# Main
# root = tree_input()
#
# h = height(root)
# print(h)