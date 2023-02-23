from PACKAGES.BINARYTREE import tree_input,print_tree,\
    print_tree_detailed,preorder_traversal,postorder_traversal,\
    level_wise_input,print_level_order


# root = tree_input()
#
# print_tree(root)
# print("Detailed Tree Printing")
# print_tree_detailed(root)
# print("Preorder Tree printing")
# preorder_traversal(root)
# print("postorder traversal")
# postorder_traversal(root)

root = level_wise_input()
print_level_order(root)

