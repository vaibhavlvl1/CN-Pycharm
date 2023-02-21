"""
 Code : All connected components
Send Feedback
Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
2. E is the number of edges present in graph G.
3. You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.

Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
Input Format :

The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two space separated integers, that denote that there exists an edge between vertex a and b.

Output Format :

Print different components in new line. And each component should be printed in increasing order of vertices (separated by space). Order of different components doesn't matter.

Constraints :

0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1

Sample Input 1:

4 2
0 1
2 3

Sample Output 1:

0 1
2 3

Sample Input 2:

4 3
0 1
1 3
0 3

Sample Output 2:

0 1 3
2


"""

import queue
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.adjMatrix)

    def connectedComponentsHelper(self, visited, smallOutput, vertex):
        visited[vertex] = True
        smallOutput.append(vertex)

        for i in range(self.nVertices):
            if self.adjMatrix[vertex][i] == 1 and not visited[i]:
                self.connectedComponentsHelper(visited, smallOutput, i)

    def allConnectedComponents(self):
        visited = [False for i in range(self.nVertices)]
        output = []

        for i in range(len(visited)):
            if not visited[i]:
                smallOutput = list()
                self.connectedComponentsHelper(visited, smallOutput, i)
                output.append(smallOutput)

        return output


# Main
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E):
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

ans = g.allConnectedComponents()

if ans != None:
    for component in ans:
        component.sort()
        for elem in component:
            print(elem, end=' ')
        print()