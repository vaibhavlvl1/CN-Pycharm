"""DFS Traversal"""

import queue


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.arr = [[0 for i in range(self.vertices)] for j in range(self.vertices)]

    def add_edge(self, v1, v2):
        self.arr[v1][v2] = 1
        self.arr[v2][v1] = 1

    def has_edge(self, v1, v2):
        if self.arr[v1][v2] > 0:
            return True
        return "No edge"

    def remove_edge(self, v1, v2):
        if not self.has_edge(v1, v2):
            "No edge or already removed"
            return
        self.arr[v1][v2] = 0
        self.arr[v2][v1] = 0

    def __str__(self):
        return self.arr.__str__()

    def __bfs_helper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True

        while not q.empty():
            u = q.get()
            print(u)
            for i in range(self.vertices):
                if self.arr[u][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.vertices)]

        for i in range(self.vertices):
            if visited[i] == False:
                self.__bfs_helper(i, visited)

    def __dfs_helper(self, sv, visited):
        visited[sv] = True
        print(sv)
        for j in range(self.vertices):
            if self.arr[sv][j] > 0 and visited[j] == False:
                visited[j] = True
                self.__dfs_helper(j, visited)

    def dfs(self):
        visited = [False for i in range(self.vertices)]
        self.__dfs_helper(0, visited)