import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed or undirected graph
# Here we create a directed graph as an example
G = nx.DiGraph()

# Add edges along with weights (costs)
G.add_weighted_edges_from([
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 3, 3),
    (3, 4, 1),
    (2, 4, 5)
])

# Perform shortest path search
start_node = 0
end_node = 4
shortest_path = nx.dijkstra_path(G, start_node, end_node)
shortest_distance = nx.dijkstra_path_length(G, start_node, end_node)

print("Shortest path from node {} to node {}: {}".format(start_node, end_node, shortest_path))
print("Shortest distance: {}".format(shortest_distance))
