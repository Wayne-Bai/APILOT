import networkx as nx
from networkx.algorithms import centrality

# Assuming G is a given graph that we've already created
# Create and populate the graph (Example)
G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.add_edge(2, 0)

# Compute HITS Authority matrix using networkx hitting algorithm
hits_matrix = nx.hITS(G)

# Now hits_matrix contains the authority centrality and hub centrality
# The matrix has a shape (number_of_nodes, 2) where,
# - hits_matrix[i, 0] is the authority score for the node i
# - hits_matrix[i, 1] is the hub centrality score for the node i

for i, j in hits_matrix.items():
    print(f"Node {i}: Authority={j[0]}, Hub={j[1]}")
