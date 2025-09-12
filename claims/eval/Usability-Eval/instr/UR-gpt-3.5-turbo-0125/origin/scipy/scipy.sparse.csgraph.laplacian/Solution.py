
import numpy as np
import scipy.sparse as sp

def laplacian_of_directed_graph(adjacency_matrix):
    out_degree = np.sum(adjacency_matrix, axis=1)
    in_degree = np.sum(adjacency_matrix, axis=0)
    laplacian_matrix = sp.diags(in_degree, 0) - adjacency_matrix
    return laplacian_matrix

# Example usage
adjacency_matrix = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
laplacian = laplacian_of_directed_graph(adjacency_matrix)
print(laplacian.toarray())
