from PACKAGES.BINARYTREE import tree_input,print_tree,\
    print_tree_detailed,preorder_traversal,postorder_traversal


root = tree_input()

print_tree(root)
print("Detailed Tree Printing")
print_tree_detailed(root)
print("Preorder Tree printing")
preorder_traversal(root)
print("postorder traversal")
postorder_traversal(root)

