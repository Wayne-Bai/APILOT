import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "E")
G.add_edge("E", "A")
G.add_edge("A", "C")

# Compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality scores
print("Node  Harmonic Centrality")
for node in harmonic_centrality:
    print(f"{node}  {harmonic_centrality[node]}")

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()

# You can also use spring layout for visualization
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
