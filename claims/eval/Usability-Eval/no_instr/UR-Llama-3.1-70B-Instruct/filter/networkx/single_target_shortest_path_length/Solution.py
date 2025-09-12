import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'C', weight=2.0)
G.add_edge('A', 'C', weight=3.0)
G.add_edge('C', 'D', weight=1.0)
G.add_edge('D', 'E', weight=2.0)
G.add_edge('E', 'F', weight=1.0)

# Specify the target node
target = 'F'

# Compute the shortest path lengths to target from all reachable nodes
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, target)

# Print the shortest path lengths
print(shortest_path_lengths)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
