from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def CompareList(li1, li2):
    L1 = len(li1)
    L2 = len(li2)
    if L1 != L2:
        return False
    for i in range(L1):
        if li1[i] != li2[i]:
            return False
    return True


def makeListofNodes(tree):
    q = queue.Queue()
    ResList = []
    q.put(tree)

    while not q.empty():
        Litem = q.get()
        ResList.append(Litem.data)

        for child in Litem.children:
            ResList.append(child.data)
            q.put(child)
    return ResList


def isIdentical(tree1, tree2):
    Tree1List = makeListofNodes(tree1)
    Tree2List = makeListofNodes(tree2)

    if CompareList(Tree1List, Tree2List):
        return True
    return False


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')



"""
This works as well i havent tried base cases of no root

def make_list(tree):
    li = []
    li.append(tree.data)
    for child in tree.children:
        temp = make_list(child)
        for ele in temp:
            li.append(ele)
    return li
        
    

def check(tree1,tree2):
    
    li1 = make_list(tree1)
    li2 = make_list(tree2)
    
    return li1==li2
"""