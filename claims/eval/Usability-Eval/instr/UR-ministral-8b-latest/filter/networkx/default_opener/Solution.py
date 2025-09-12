import networkx as nx
import os

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]

for node, edge in edges:
    G.add_edge(node, edge)

# Display the graph
print("The graph:")
nx.draw(G, with_labels=True)
