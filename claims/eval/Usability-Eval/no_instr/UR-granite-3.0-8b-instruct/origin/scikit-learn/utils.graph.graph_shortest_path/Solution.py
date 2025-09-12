from scipy.sparse.csgraph import dijkstra

# Assuming you have a graph represented as an adjacency matrix
# Replace the following line with your actual graph data
graph = [[0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

# Replace the following line with the starting node
start_node = 0

# Perform the shortest path search
distances, predecessors = dijkstra(csgraph=graph, indices=start_node)

# Print the results
for node, distance in enumerate(distances):
    print(f"Node {node}: {distance}")
