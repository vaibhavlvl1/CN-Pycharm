# """
# def intersection(x_list,y_list):
#     result = []
#     for i in range(len(x_list)):
#         for j in range(len(y_list)):
#             if x_list[i] == y_list[j]:

#                 result.append(x_list[i])
#                 break
#     return result
# """


# def intersection(y_list, x_list):
#     lst3 = [x for x in y_list if x in x_list]
#     return lst3


# t = int(input())

# for i in range(1, t + 1):

#     n1 = int(input())
#     if n1==0:
#         x_list=[]
#     else:
#         x_list = [int(x) for x in input().split()]

#     n2 = int(input())
#     if n2==0:
#         y_list =[]
#     else:
#         y_list = [int(y) for y in input().split()]

#     x = intersection(x_list,y_list)
#     for ele in x:
#         print(ele,end=" ")


#     print()

import sys


def intersections(arr1, n, arr2, m):
    #     #Your code goes here
    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j]:
                print(arr1[i], end=' ')
                arr2[j] = sys.maxsize
                break


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1