
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Compute spring layout
pos = nx.spring_layout(G)

# Scale positions
scaled_pos = {node: (pos[node][0] * 100, pos[node][1] * 100) for node in pos}

print(scaled_pos)
