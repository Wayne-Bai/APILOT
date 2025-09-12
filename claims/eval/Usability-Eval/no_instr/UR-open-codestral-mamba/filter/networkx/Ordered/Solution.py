"""
Importing the necessary modules using python
"""
import networkx as nx

# Creating an empty order-preserving Graph
G = nx.Graph()

# Adding nodes to the graph
node1 = "Node1"
node2 = "Node2"
node3 = "Node3"
node4 = "Node4"
G.add_node(node1)
G.add_node(node2)
G.add_node(node3)
G.add_node(node4)

# Adding edges to the graph
edge1 = (node1, node2)
edge2 = (node2, node3)
edge3 = (node3, node4)
G.add_edge(*edge1)
G.add_edge(*edge2)
G.add_edge(*edge3)

# Printing nodes and edges
print("Nodes:", G.nodes())
print("Edges:", list(G.edges()))
