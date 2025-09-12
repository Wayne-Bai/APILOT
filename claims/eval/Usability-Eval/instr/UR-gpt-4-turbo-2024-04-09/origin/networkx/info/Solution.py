import networkx as nx

# create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (3, 4), (4, 2)])

# Print short summary of information for the entire graph
print(nx.info(G))

# Optionally, to print information for a specific node
node = 3
print(f"Information for node {node}:")
print(f"Degree of node {node}: {G.degree(node)}")
