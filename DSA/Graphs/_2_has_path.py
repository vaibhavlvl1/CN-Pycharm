"""
 Code : Has Path
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. Print true if the path exists and false otherwise.
Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
2. E is the number of edges present in graph G.

Input Format :

The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
The following line contain two integers, that denote the value of v1 and v2.

Output Format :

The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.

Constraints :

0 <= V <= 1000
0 <= E <= 1000
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= V - 1
0 <= v2 <= V - 1
Time Limit: 1 second

Sample Input 1 :

4 4
0 1
0 3
1 2
2 3
1 3

Sample Output 1 :

true

Sample Input 2 :

6 3
5 3
0 1
3 4
0 3

Sample Output 2 :

false


"""

from sys import stdin
import queue


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self):
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

    def __hasPath(self, sv, ev, visited):
        if sv == ev:
            return True

        q = queue.Queue()
        q.put(sv)
        visited[sv] = True

        while q.empty() is False:
            u = q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[u][i] == 1 and not visited[i]:
                    if i == ev:
                        return True

                    q.put(i)
                    visited[i] = True
        return False

    def hasPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPath(sv, ev, visited)

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

li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])

if g.hasPath(sv, ev):
    print('true')
else:
    print('false')