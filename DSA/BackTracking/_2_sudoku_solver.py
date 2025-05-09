"""
 Sudoku Solver
Send Feedback
Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.
Input Format :

9 Lines where ith line contains ith row elements separated by space

Output Format :

 true or false

Sample Input :

9 0 0 0 2 0 7 5 0
6 0 0 0 5 0 0 4 0
0 2 0 4 0 0 0 1 0
2 0 8 0 0 0 0 0 0
0 7 0 5 0 9 0 6 0
0 0 0 0 0 0 4 0 1
0 1 0 0 0 5 0 8 0
0 9 0 0 7 0 0 0 4
0 8 2 0 4 0 0 0 6

Sample Output :

true


"""


def presentInRow(board, row, num):
    for j in range(9):
        if board[row][j] == num:
            return True
    return False


def presentInCol(board, col, num):
    for j in range(9):
        if board[j][col] == num:
            return True
    return False


def presentInBox(board, row, col, num):
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == num:
                return True
    return False


def isPossible(board, row, col, num):
    if (presentInRow(board, row, num)):
        return False
    if (presentInCol(board, col, num)):
        return False
    if (presentInBox(board, row - (row % 3), col - (col % 3), num)):
        return False
    return True


def solveSudoku(board):
    row = -1
    col = -1
    flag = False
    for i in range(9):
        for j in range(9):
            if board[i][j] is 0:
                row = i
                col = j
                flag = True
                break
        if flag is True:
            break
    if row == -1:
        return True
    for num in range(1, 10):
        if (isPossible(board, row, col, num)):
            board[row][col] = num
            if (solveSudoku(board) is True):
                return True
            board[row][col] = 0

    return False


board = [[int(ele) for ele in input().split()] for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')



"""
Easy Method

"""

grid = [[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]


def possible(row, col, number):
    global grid
    for i in range(9):
        if grid[row][i] == number:
            return False

    for i in range(9):
        if grid[i][col] == number:
            return False

    x0 = (col // 3) * 3
    y0 = (row // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global grid
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for number in range(1, 10):
                    if possible(row, col, number):
                        grid[row][col] = number
                        solve()
                        grid[row][col] = 0
                return

    for row in grid:
        print(row)
    print("-----------------------Other Solutions---------------------------------")




