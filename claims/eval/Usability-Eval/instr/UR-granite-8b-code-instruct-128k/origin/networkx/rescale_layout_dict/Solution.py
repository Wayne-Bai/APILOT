import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Use the spring layout algorithm to generate the positions
pos = nx.spring_layout(G)

# Scale the positions to a range of 0 to 1
scaled_pos = {k: (v[0]/50, v[1]/50) for k, v in pos.items()}

# Print the scaled positions
print(scaled_pos)
