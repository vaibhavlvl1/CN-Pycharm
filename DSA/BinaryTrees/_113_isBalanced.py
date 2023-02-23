"""
this checks if the tree is balanced or not
i.e. if the height diff between right side and left side is less or equal to 1
for each node
"""

from PACKAGES.BINARYTREE import tree_input,print_tree
from DSA.BinaryTrees._5_height_of_tree import height


def isBalanced(root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    leftside = isBalanced(root.left)
    rightside = isBalanced(root.right)

    return leftside or rightside

root = tree_input()
print(isBalanced(root))