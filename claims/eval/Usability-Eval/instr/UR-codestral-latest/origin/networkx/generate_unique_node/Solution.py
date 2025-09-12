import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes with unique labels
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Print the nodes of the graph
print(G.nodes())
