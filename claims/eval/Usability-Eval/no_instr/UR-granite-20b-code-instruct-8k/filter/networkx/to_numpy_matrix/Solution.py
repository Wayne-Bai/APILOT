import networkx as nx

# create an empty graph
G = nx.Graph()

# add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# add edges to the graph
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E')])

# convert the graph to a NumPy matrix
adj_matrix = nx.adjacency_matrix(G)

# print the adjacency matrix
print(adj_matrix.todense())
