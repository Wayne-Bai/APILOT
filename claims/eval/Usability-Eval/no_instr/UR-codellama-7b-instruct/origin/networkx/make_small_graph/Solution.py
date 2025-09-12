
import networkx as nx

# Define the graph structure
graph_description = "A directed graph with 5 nodes and 7 edges"
G = nx.DiGraph()

# Add nodes to the graph
for i in range(5):
    G.add_node(i)

# Add edges to the graph
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4)]
for edge in edges:
    G.add_edge(*edge)
