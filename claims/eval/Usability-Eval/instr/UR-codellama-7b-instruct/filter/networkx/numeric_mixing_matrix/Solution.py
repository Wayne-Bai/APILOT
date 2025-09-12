import networkx as nx

# Define a simple graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('B', 'C')])

# Compute the numeric mixing matrix
num_mixing = nx.numeric_mixing(G)

print(num_mixing)
