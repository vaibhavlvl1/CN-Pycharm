from PACKAGES.BINARYTREE import tree_input


def changeToDepthTree(root, k=0):
    if root is None:
        return

    root.data = k

    changeToDepthTree(root.left, k=k + 1)
    changeToDepthTree(root.right, k=k + 1)




def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


# Main
root = tree_input()

changeToDepthTree(root)
inOrder(root)