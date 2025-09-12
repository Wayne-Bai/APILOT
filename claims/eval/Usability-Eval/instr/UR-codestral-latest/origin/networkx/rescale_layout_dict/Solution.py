import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Compute node positions with spring layout
pos = nx.spring_layout(G)

# Scale the positions to the range [0.0, 1.0]
pos_scaled = dict((k, (v[0]/max(pos.values(), key=lambda x: x[0])[0], v[1]/max(pos.values(), key=lambda x: x[1])[1])) for k, v in pos.items())

print(pos_scaled)
