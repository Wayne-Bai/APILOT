import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2, weight=2)
G.add_edge(2, 3, weight=5)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 1, weight=6)
G.add_edge(1, 3, weight=3)
G.add_edge(2, 4, weight=4)

# Compute eccentricity (maximum distance from a node to all other nodes)
ecc = nx.eccentricity(G)
print("Eccentricity:", ecc)

# Compute diameter (maximum eccentricity)
diameter = max(ecc.values())
print("Diameter:", diameter)

# Compute radius (minimum eccentricity)
radius = min(ecc.values())
print("Radius:", radius)

# Compute periphery (nodes with eccentricity equal to the diameter)
periphery = [node for node, value in ecc.items() if value == diameter]
print("Periphery:", periphery)

# Compute center (nodes with eccentricity equal to the radius)
center = [node for node, value in ecc.items() if value == radius]
print("Center:", center)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
