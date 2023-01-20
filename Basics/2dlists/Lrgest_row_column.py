'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    # for row
    max = -1
    row = 0
    x = ''

    if nRows == 0 or mCols == 0:
        print(("row" + " " + "0" + " " + "-2147483648"))

    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum = sum + arr[i][j]

            if max < sum:
                max = sum
                row = i
        x = ("row" + " " + str(row) + " " + str(max))

    # for cols
    max2 = -1
    col = 0
    y = ''
    # sum = 0
    for j in range(mCols):
        sum = 0
        for i in range(nRows):
            sum = sum + arr[i][j]

            if max2 < sum:
                col = j
                max2 = sum
        y = ("column" + " " + str(col) + " " + str(max2))

    if max > max2:
        print(x)
    elif max == max2:
        print(x)
    else:
        print(y)


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1