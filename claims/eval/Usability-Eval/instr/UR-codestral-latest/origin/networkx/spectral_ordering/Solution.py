import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (5, 6), (6, 5)])

# Compute the Laplacian matrix of the graph
L = nx.laplacian_matrix(G)

# Compute the Fiedler vector (the eigenvector corresponding to the second-smallest eigenvalue)
eigvals, eigvecs = nx.linalg.algebraicconnectivity.fiedler_vector(L)

# Get the node ordering based on the Fiedler vector
node_ordering = [node for node, _ in sorted(zip(G.nodes, eigvecs), key=lambda x: x[1])]

print("Spectral ordering of the nodes: ", node_ordering)
