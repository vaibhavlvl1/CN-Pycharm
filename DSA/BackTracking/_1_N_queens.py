"""
 N-Queens
Send Feedback
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
Input Format :

Line 1 : Integer N

Output Format :

One Line for every board configuration.
Every line will have N*N board elements printed row wise and are separated by space

Note : Don't print anything if there isn't any valid configuration.
Constraints :
1<=N<=10
Sample Input 1:

4

Sample Output 1 :

0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0
0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0


"""


def isSafe(row, col, board, n):
    # vertical direction
    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i -= 1
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def printPathsHelper(row, n, board):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
        print()
        return
    for col in range(n):
        if isSafe(row, col, board, n) is True:
            board[row][col] = 1
            printPathsHelper(row + 1, n, board)
            board[row][col] = 0
    return


def nQueen(n):
    board = [[0 for j in range(n)] for i in range(n)]
    printPathsHelper(0, n, board)


n = int(input())
nQueen(n)




# method 1

def solve_n_queen(n):
    col = set()
    pos_diag = set()
    neg_diag = set()

    res = []

    board = [["."]*n for i in range(n)]
    print(board)

    def backtrack(r):
        if r==n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or r+c in pos_diag or r-c in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)

            board[r][c]= "Q"

            backtrack(r+1)

            col.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c]= "."
    backtrack(0)
    return res



# method 2

# method 2

n = int(input("chess board size"))

board = [[0] * n for i in range(n)]


def check_col(board, row, col):
    for i in range(row, -1, -1):
        if board[i][col] == 1:
            return False
    return True


def check_diag(board, row, col):
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def nqn(board, row):
    if row == n:
        return True

    for i in range(n):
        if check_col(board, row, i) == True and check_diag(board, row, i) == True:
            board[row][i] = 1
            if nqn(board, row + 1):
                return True
            board[row][i] = 0
    return False


nqn(board, 0)

for row in board:
    print(row)