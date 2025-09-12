import networkx as nx
import matplotlib.pyplot as plt

# Create an ordered directed graph
G_1 = nx.DiGraph()
G_1.add_node(1)
G_1.add_node(2)
G_1.add_node(3)
G_1.add_edge(1, 2)
G_1.add_edge(2, 3)

# Create an ordered multi-diagraph
G_2 = nx.MultiDiGraph()
G_2.add_node(1)
G_2.add_node(2)
G_2.add_node(3)
G_2.add_edge(1, 2)
G_2.add_edge(2, 3)

# Create an ordered multi-graph
G_3 = nx.MultiGraph()
G_3.add_node(1)
G_3.add_node(2)
G_3.add_node(3)
G_3.add_edge(1, 2)
G_3.add_edge(2, 3)

# Print nodes and edges for each graph
print("Nodes and Edges for DiGraph:")
print("Nodes:", list(G_1.nodes))
print("Edges:", list(G_1.edges))

print("\nNodes and Edges for MultiDiGraph:")
print("Nodes:", list(G_2.nodes))
print("Edges:", list(G_2.edges))

print("\nNodes and Edges for MultiGraph:")
print("Nodes:", list(G_3.nodes))
print("Edges:", list(G_3.edges))
