from sklearn.utils.graph_shortest_path import graph_shortest_path

# Example graph represented as an adjacency matrix
# Here infinity (a large number, e.g., float('inf')) is used to denote no direct path between nodes
# The graph can be directed or undirected
graph = [
    [0, 1, 4, float('inf'), float('inf')],
    [1, 0, 2, 6, float('inf')],
    [4, 2, 0, 3, 2],
    [float('inf'), 6, 3, 0, 1],
    [float('inf'), float('inf'), 2, 1, 0]
]

# Calculate the shortest path using the Floyd-Warshall algorithm
# method 'FW': Floyd-Warshall
# directed: Set True for a directed graph, False for undirected
shortest_paths = graph_shortest_path(graph, method='FW', directed=True)

print("Shortest paths matrix:")
print(shortest_paths)
