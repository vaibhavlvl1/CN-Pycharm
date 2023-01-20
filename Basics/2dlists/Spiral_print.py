from sys import stdin


def spiralPrint(mat, nRows, mCols):
    a = 0
    b = 0
    while (a < nRows and b < mCols):
        for i in range(b, mCols):
            print(mat[a][i], end=" ")
        a += 1

        for i in range(a, nRows):
            print(mat[i][mCols - 1], end=" ")
        mCols -= 1

        for i in range(mCols - 1, b - 1, -1):
            print(mat[nRows - 1][i], end=" ")
        nRows -= 1

        for i in range(nRows - 1, a - 1, -1):
            print(mat[i][b], end=" ")
        b += 1

    # Your code goes here


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1