import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'C', weight=2.0)
G.add_edge('A', 'C', weight=3.0)
G.add_edge('C', 'D', weight=4.0)
G.add_edge('D', 'E', weight=1.0)
G.add_edge('A', 'E', weight=6.0)

# Compute shortest paths
shortest_paths = nx.shortest_path(G, weight='weight')

# Compute shortest path lengths
shortest_path_lengths = nx.shortest_path_length(G, weight='weight')

# Print shortest path lengths
for node in G.nodes:
    print(f'Shortest path lengths from {node}:')
    for neighbor in G.nodes:
        if node!= neighbor:
            print(f'  to {neighbor}: {shortest_path_lengths[node][neighbor]}')

# Highlight shortest path in the graph
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()
