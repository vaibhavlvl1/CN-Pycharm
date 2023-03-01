import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def constructBST(arr):
    """
    input a sorted array
    :return: BST root
    """
    if len(arr) == 0:
        return None

    mid = len(arr)//2
    root_data = arr[mid]
    root = BinaryTreeNode(root_data)

    root.left = constructBST(arr[:mid])
    root.right = constructBST(arr[mid+1:])

    return root


def level_order_print(root):
    if root is None:
        return None
    print(root.data)
    q = queue.Queue()
    q.put(root)
    q.put(None)

    while not q.empty():
        curr = q.get()

        if curr != None:
            if curr.left is not None and curr.left.data !=-1:
                q.put(curr.left)
                print(curr.left.data,end="")
            if curr.right is not None and curr.right.data != -1:
                q.put(curr.right)
                print(curr.right.data,end="")
        else:
            if q.empty():
                break
            q.put(None)
            print()

def level_order_input():
    data = int(input())
    if data == -1:
        return None
    root = BinaryTreeNode(data)
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        curr = q.get()

        if curr != -1:
            left_data = int(input())
            left_node = BinaryTreeNode(left_data)
            if left_node.data != -1:
                curr.left = left_node
                q.put(left_node)

            right_data = int(input())
            right_node = BinaryTreeNode(right_data)
            if right_node.data != -1:
                curr.right = right_node
                q.put(right_node)

    return root


