"""
import sys
sys.setrecursionlimit(10 ** 8)


def subsetsum(arr, k) :
    n = len(arr)
    if n==1:
        if arr[0]==k:
            output = [[k]]
            return output
        else:
            output = []
            return output



    output1 = subsetsum(arr[:-1],k)
    output2 = subsetsum(arr[:-1],k-arr[-1])

    for list in output2:
        list.append(arr[-1])
    if arr[-1] ==k:
        output2.append([k])

    return output1+output2























#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsum(arr, k)

    printListOfList(liOfLi)


"""


def subset(arr):
    n = len(arr)
    if n == 0:
        return [""]

    smalloutput = subset(arr[1:])

    output = []
    for sub in smalloutput:
        output.append(sub)

    for sub in smalloutput:
        output.append(str(arr[0]) + " " + str(sub))

    return output


n = int(input())

arr = [int(x) for x in input().split()]

ans = subset(arr)

for i in ans:
    print(i)