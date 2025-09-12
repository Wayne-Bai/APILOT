import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Iterate over the nodes in the graph
for node in G:
    print(node)

# Get the number of nodes in the graph
print(G.number_of_nodes())
