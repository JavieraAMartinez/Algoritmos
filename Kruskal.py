class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((w, u, v))
    edges.sort()

    n = len(graph)
    mst = []
    ds = DisjointSet(n)

    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

graph = {
    0: {1: 2, 2: 3},
    1: {0: 2, 2: 1, 3: 1},
    2: {0: 3, 1: 1, 3: 4},
    3: {1: 1, 2: 4}
}
print("Minimum spanning tree:")
print(kruskal(graph))
