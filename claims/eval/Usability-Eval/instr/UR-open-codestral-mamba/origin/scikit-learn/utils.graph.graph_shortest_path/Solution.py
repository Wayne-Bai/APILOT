import numpy as np

# Adjacency matrix
graph = np.array([[0, 10, 20, 0],
                  [10, 0, 5, 16],
                  [20, 5, 0, 20],
                  [0, 16, 20, 0]])

# Number of vertices in the graph
V = len(graph)

# Function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minDistance(dist, sptSet):
    min_val = np.inf
    min_index = -1

    for v in range(V):
        if dist[v] < min_val and sptSet[v] == False:
            min_val = dist[v]
            min_index = v
    return min_index

# Function to find the shortest path from source to all vertices
def dijkstra(graph, src):
    dist = [np.inf] * V
    dist[src] = 0
    sptSet = [False] * V

    for _ in range(V - 1):
        u = minDistance(dist, sptSet)
        sptSet[u] = True

        for v in range(V):
            if (graph[u][v] > 0 and sptSet[v] == False and
                dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]

    return dist

print("Shortest distances from node 0:", dijkstra(graph, 0))
print("Shortest distances from node 3:", dijkstra(graph, 3))
