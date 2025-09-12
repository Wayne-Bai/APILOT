import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.karate_club_graph()

# Get the positions of the nodes by using fruit ultimo layout
positions = nx.spring_layout(G)

# Scale the positions
for node, pos in positions.items():
    positions[node] = (pos[0] * 1.5, pos[1] * 1.5)

# Return the dictionary of scaled positions
scaled_positions = positions
scaled_positions
