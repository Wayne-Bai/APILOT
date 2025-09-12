import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Add edges to the graph
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')])

# Define the labels for each node
nx.set_node_attributes(G, {'A': 0, 'B': 0, 'C': 1, 'D': 1, 'E': 2})

# Perform label propagation
nx.label_propagation_communities(G)
