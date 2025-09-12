import networkx as nx
import matplotlib.pyplot as plt

# Creating a sample graph
G = nx.Graph()

# Adding nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Adding edges to the graph
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "A")

# Creating a node
n = "D"

# Printing short summary of information for the graph G
print("Summary of graph G:")
print("  Number of nodes:", G.number_of_nodes())
print("  Number of edges:", G.number_of_edges())
print("  Graph name:", type(G).__name__)

# Printing short summary of information for the node n
print("\nSummary of node", n + ":")
print("  Node name:", n)
print("  Degree:", G.degree(n))
print("  Neighbours:", list(G.neighbors(n)))

# Drawing the graph
nx.draw(G, with_labels=True)
plt.show()
