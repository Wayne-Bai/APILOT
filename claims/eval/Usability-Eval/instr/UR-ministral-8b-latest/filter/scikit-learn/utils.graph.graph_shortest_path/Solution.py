import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import pairwise_distances
from heapq import heappush, heappop

np.random.seed(0)

# Generating random data for demonstration
X = np.random.rand(10, 2)

# Perform k-means clustering using MiniBatchKMeans
kb = MiniBatchKMeans(n_clusters=3, random_state=0).fit(X)
labels = kb.labels_
clusters = [X[labels == i] for i in range(3)]

# Calculate pairwise distances between data points in each cluster
cluster_distances = [pairwise_distances(cluster, metric='euclidean') for cluster in clusters]

# Function to find shortest path in a graph
def shortest_path(graph, start, end):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        (dist, current_node) = heappop(priority_queue)

        if current_node == end:
            return dist

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    heappush(priority_queue, (dist + weight, neighbor))

    return float('inf')

# Example Graph represented as adjacency list
graph = {
    'A': { 'B': 1, 'C': 4 },
    'B': { 'A': 1, 'C': 2, 'D': 5 },
    'C': { 'A': 4, 'B': 2, 'D': 1 },
    'D': { 'B': 5, 'C': 1 }
}

# Find the shortest path from 'A' to 'C'
start_node = 'A'
end_node = 'C'
print(shortest_path(graph, start_node, end_node))
