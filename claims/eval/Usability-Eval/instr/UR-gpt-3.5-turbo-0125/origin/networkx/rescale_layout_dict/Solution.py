
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1,2), (2,3), (3,1)])

# Calculate the spring layout
pos = nx.kamada_kawai_layout(G)

# Scale the positions
scale = 2
scaled_pos = {node: (pos[node][0] * scale, pos[node][1] * scale) for node in pos}

print(scaled_pos)
