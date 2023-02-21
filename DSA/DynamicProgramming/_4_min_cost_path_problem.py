"""
 Min Cost Path Problem
Send Feedback
An integer matrix of size (M x N) has been given. Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:

1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"

The cost of a path is defined as the sum of each cell's values through which the route passes.
 Input format :

The first line of the test case contains two integer values, 'M' and 'N', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

The second line onwards, the next 'M' lines or rows represent the ith row values.

Each of the ith row constitutes 'N' column values separated by a single space.

Output format :

Print the minimum cost to reach the destination.

Constraints :

1 <= M <= 10 ^ 2
1 <= N <=  10 ^ 2

Time Limit: 1 sec

Sample Input 1 :

3 4
3 4 1 2
2 1 8 9
4 7 8 1

Sample Output 1 :

13

Sample Input 2 :

3 4
10 6 9 0
-23 8 9 90
-200 0 89 200

Sample Output 2 :

76

Sample Input 3 :

5 6
9 6 0 12 90 1
2 7 8 5 78 6
1 6 0 5 10 -4
9 6 2 -10 7 4
10 -2 0 5 5 7

Sample Output 3 :

18


"""

from sys import stdin

MAX_VALUE = 2147483647


def minCostPath(cost, n, m):
    dp = [[MAX_VALUE for j in range(m + 1)] for j in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 and j == m - 1:
                dp[i][j] = cost[i][j]
            else:
                ans1 = dp[i + 1][j]
                ans2 = dp[i][j + 1]
                ans3 = dp[i + 1][j + 1]
                dp[i][j] = cost[i][j] + min(ans1, ans2, ans3)
    return dp[0][0]


# taking input using fast I/O method
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    n = int(li[0])
    m = int(li[1])

    if n == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(n)]
    return mat, n, m


# main
mat, n, m = take2DInput()
print(minCostPath(mat, n, m))