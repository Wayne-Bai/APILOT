import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
graph = nx.DiGraph()

# Add nodes and edges (with weights)
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 3, 3)
]

graph.add_weighted_edges_from(edges)

# Perform shortest path search using Dijkstra's algorithm
start_node = 0
end_node = 3
shortest_path = nx.dijkstra_path(graph, start_node, end_node)
shortest_distance = nx.dijkstra_path_length(graph, start_node, end_node)

# Print results
print("Shortest path from node {} to node {}: {}".format(start_node, end_node, shortest_path))
print("Shortest distance: {}".format(shortest_distance))

# Optional: Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
