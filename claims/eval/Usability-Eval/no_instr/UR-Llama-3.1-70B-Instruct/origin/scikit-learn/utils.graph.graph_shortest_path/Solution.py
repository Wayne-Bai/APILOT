# Import necessary libraries, no scikit-learn, instead NetworkX library
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.DiGraph()

# Add edges to the graph with their respective weights
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)

# Define the start and end nodes
start_node = 'A'
end_node = 'D'

# Perform Dijkstra's algorithm to find the shortest path
try:
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
except nx.NetworkXNoPath:
    print("No path found between the nodes.")
else:
    print("Shortest path:", shortest_path)

# Calculate the shortest path length
shortest_path_length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')
print("Shortest path length:", shortest_path_length)

# Position the nodes for plotting
pos = nx.spring_layout(G)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=20)

# Draw the edges
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')

# Draw the edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the plot
plt.show()
