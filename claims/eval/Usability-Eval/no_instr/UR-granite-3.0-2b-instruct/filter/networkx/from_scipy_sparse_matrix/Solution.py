import networkx as nx

# Assuming adj_list is your scipy sparse matrix adjacency list
# Convert scipy sparse matrix to networkx graph
G = nx.from_scipy_sparse_matrix(adj_list)
