def floyd(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u in range(n):
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = {
    0: {1: 3, 2: 8},
    1: {2: -4, 3: 1},
    2: {3: 7, 0: 2},
    3: {0: -5, 1: 6}
}
print("All pairs shortest distances:")
for row in floyd(graph):
    print(row)
