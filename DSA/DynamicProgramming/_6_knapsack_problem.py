"""
 0 1 Knapsack - Problem
Send Feedback
A thief robbing a store can carry a maximal weight of W into his knapsack. There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the maximum value V, that the thief can steal?
Input Format :

The first line of the input contains an integer value N, which denotes the total number of items.

The second line of input contains the N number of weights separated by a single space.

The third line of input contains the N number of values separated by a single space.

The fourth line of the input contains an integer value W, which denotes the maximum weight the thief can steal.

Output Format :

Print the maximum value of V that the thief can steal.

Constraints :

1 <= N <= 20
1<= Wi <= 100
1 <= Vi <= 100

Time Limit: 1 sec

Sample Input 1 :

4
1 2 4 5
5 4 8 6
5

Sample Output 1 :

13

Sample Input 2 :

5
12 7 11 8 9
24 13 23 15 16
26

Sample Output 2 :

51


"""

from sys import stdin


def knapsack(W, val, wt):
    n = len(val)
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j < wt[i - 1]:
                ans = dp[i - 1][j]
            else:
                ans1 = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                ans2 = dp[i - 1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans
    return dp[n][W]


n = int(input())
wt = [int(i) for i in input().split()]
val = [int(i) for i in input().split()]
W = int(input())
ans = knapsack(W, val, wt)
print(ans)