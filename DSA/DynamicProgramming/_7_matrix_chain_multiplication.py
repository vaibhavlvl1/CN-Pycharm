"""
 Matrix Chain Multiplication
Send Feedback
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.
Input Format:

The first line of input contains an integer, that denotes the value of n. The following line contains n+1 integers, that denote the value of elements of array p[].

Output Format:

The first and only line of output prints the minimum number of multiplication needed.

Constraints :

1 <= n <= 100
Time limit: 1 second

Sample Input 1:

3
10 15 20 25

Sample Output 1:

8000

Sample Output Explanation:

There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000.


"""

import sys
sys.setrecursionlimit (10**8)
from sys import stdin
def mcm(p,n):
	n+=1
	m=[[sys.maxsize for i in range (0,n+1)] for j in range (0,n+1)]
	for i in range (1,n):
		m[i][i]=0
	for l in range (2,n):
		for i in range (1,n-l+1):
			j=i+l-1
			for k in range (i,j):
				q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
				if(q<m[i][j]):
					m[i][j]=q
	return m[1][n-1]











n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
print(mcm(p,n))