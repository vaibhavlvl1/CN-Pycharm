from PACKAGES.BINARYSEARCHTREE import level_order_input,level_order_print

def getMin(root):
    if root is None:
        return 100000

    leftmin = getMin(root.left)
    rightmin = getMin(root.right)

    return min(leftmin,rightmin,root.data)


def getMax(root):
    if root is None:
        return -1000000
    leftmax = getMax(root.left)
    rightmax = getMax(root.right)

    return max(leftmax,rightmax,root.data)

def checkBST(root):
    if root is None:
        return True

    leftMax = getMax(root.left)
    rightmin = getMin(root.right)

    if root.data>rightmin or root.data <= leftMax:
        return False
    isBSTleft = checkBST(root.left)
    isBSTright = checkBST(root.right)

    return isBSTright and isBSTleft

root = level_order_input()

print(checkBST(root))