import networkx as nx
from scipy.sparse import csr_matrix

def adjacency_matrix_as_sparse(graph):
    # Get the adjacency matrix as a dense NumPy array
    dense_matrix = nx.to_numpy_array(graph)
    # Convert to a SciPy sparse matrix
    sparse_matrix = csr_matrix(dense_matrix)
    return sparse_matrix
