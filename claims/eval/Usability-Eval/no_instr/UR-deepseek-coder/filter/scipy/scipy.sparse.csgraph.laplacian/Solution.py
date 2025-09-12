import numpy as np
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import inv

def laplacian_of_directed_graph(adj_matrix):
    # Ensure the adjacency matrix is in CSR format
    if not isinstance(adj_matrix, csr_matrix):
        adj_matrix = csr_matrix(adj_matrix)
    
    # Compute the out-degree matrix
    out_degree = np.array(adj_matrix.sum(axis=1)).flatten()
    out_degree_matrix = diags(out_degree, 0)
    
    # Compute the in-degree matrix
    in_degree = np.array(adj_matrix.sum(axis=0)).flatten()
    in_degree_matrix = diags(in_degree, 0)
    
    # Compute the Laplacian matrix for a directed graph
    laplacian = out_degree_matrix - adj_matrix
    
    return laplacian

# Example usage:
# adj_matrix = csr_matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
# laplacian = laplacian_of_directed_graph(adj_matrix)
# print(laplacian.toarray())
