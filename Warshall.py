def warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if j in graph[i] else float('inf') for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = {
    0: {1: 3, 2: 8},
    1: {2: -4, 3: 1},
    2: {3: 7},
    3: {}
}
print("All pairs shortest distances:")
for row in warshall(graph):
    print(row)

