from PACKAGES.BINARYTREE import tree_input


def countNodesGreaterThanX(root, x):
    c = 0
    if root is None:
        return 0
    if root.data > x:
        c = c + 1

    leftcount = countNodesGreaterThanX(root.left, x)
    rightcount = countNodesGreaterThanX(root.right, x)

    return c + leftcount + rightcount





# Main
root = tree_input()
x = int(input())

count = countNodesGreaterThanX(root, x)
print(count)