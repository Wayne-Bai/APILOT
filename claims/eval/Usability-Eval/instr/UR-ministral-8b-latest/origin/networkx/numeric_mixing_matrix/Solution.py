import networkx as nx

def numeric_mixing_matrix(G):
    A = nx.adjacency_matrix(G)
    D = nx.diagonal_matrix(G.degree())
    D_inv = nx.inverse_matrix(D)
    return D_inv @ A @ D_inv

# Example usage
# Create a graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])

# Get the numeric mixing matrix
nmm = numeric_mixing_matrix(G)
print(nmm)
