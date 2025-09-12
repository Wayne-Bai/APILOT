import networkx as nx
from scipy.sparse import csr_matrix

def create_graph_from_sparse_matrix(sparse_matrix):
    # Create a graph from the SciPy sparse matrix using NetworkX
    G = nx.from_scipy_sparse_array(sparse_matrix)
    return G

# Example usage with a small adjacency matrix
data = [1, 1, 1]  # values of non-zero entries
rows = [0, 1, 2]  # row indices of non-zero entries
cols = [1, 2, 0]  # column indices of non-zero entries

# Create a CSR (Compressed Sparse Row) matrix
adj_matrix = csr_matrix((data, (rows, cols)), shape=(3, 3))

# Create graph
G = create_graph_from_sparse_matrix(adj_matrix)

# Print the edges of the graph
print(list(G.edges))
