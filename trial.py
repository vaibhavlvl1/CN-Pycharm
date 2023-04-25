import queue


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arr = [[0 for i in range(self.vertices)] for j in range(self.vertices)]

    def add_edge(self, v1, v2):
        self.arr[v1][v2] = 1
        self.arr[v2][v1] = 1
        return f"Edge added between{v1} {v2}"

    def remove_edge(self, v1, v2):
        if self.has_edge(v1, v2):
            self.arr[v1][v2] = 0
            self.arr[v2][v1] = 0
        else:
            return "edge doesnt exist"

    def has_edge(self, v1, v2):
        if self.arr[v1][v2] != 0:
            return True
        return False

    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.arr[i][j], end=" ")
            print()

    def simple_input(self, edges):
        for i in range(edges):
            v1, v2 = [int(x) for x in input().split()]
            self.add_edge(v1, v2)

    def dfs_helper(self, sv, visited):
        visited[sv] = True
        print(sv)

        for i in range(self.vertices):
            if self.arr[sv][i] > 0 and visited[i] == False:
                self.dfs_helper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.vertices)]
        for i in range(self.vertices):
            if visited[i] == False:
                self.dfs_helper(i, visited)
        print()

    def bfs_helper(self, sv, visited):

        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while not q.empty():
            front = q.get()
            print(front)

            for i in range(self.vertices):
                if self.arr[sv][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.vertices)]
        for i in range(self.vertices):
            if visited[i] == False:
                self.bfs_helper(i, visited)



d = Graph(8)
d.simple_input(7)
d.bfs()