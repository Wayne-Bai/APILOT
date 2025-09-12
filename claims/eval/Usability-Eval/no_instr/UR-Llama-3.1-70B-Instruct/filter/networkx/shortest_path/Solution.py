import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add edges with their respective weights
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'C', weight=2.0)
G.add_edge('A', 'C', weight=3.0)
G.add_edge('C', 'D', weight=4.0)
G.add_edge('D', 'E', weight=5.0)
G.add_edge('E', 'A', weight=6.0)

# Compute shortest paths in the graph
shortest_paths = nx.shortest_path_length(G, weight='weight')

# Print the shortest paths from each node to every other node
for node in G.nodes:
    print(f'Shortest paths from {node}:')
    for destination, length in shortest_paths[node].items():
        if destination!= node:
            print(f'  - To {destination}: {length} units')
    print()

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
