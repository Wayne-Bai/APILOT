import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "E")
G.add_edge("E", "A")

# Print short summary of the graph G
print("Graph Information:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is the graph empty? {G.is_empty()}")
print(f"Is the graph directed? {G.is_directed()}")
print(f"Is the graph simple? {G.is_simple()}")
print()

# Print short summary of a specific node n
n = "D"
print(f"Node {n} Information:")
print(f"Degree of {n}: {G.degree(n)}")
print(f"Neighbors of {n}: {G.neighbors(n)}")
print(f"Is {n} connected to node A? {n in G.neighbors('A') or 'A' in G.neighbors(n)}")

# Draw the graph
plt.figure(figsize=(10,10))
nx.draw(G, with_labels=True)
plt.show()
