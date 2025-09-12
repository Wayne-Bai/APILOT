
import numpy as np
import scipy.sparse as sp

def laplacian_of_directed_graph(adjacency_matrix):
    out_degree = np.sum(adjacency_matrix, axis=1)
    in_degree = np.sum(adjacency_matrix, axis=0)

    diagonal = out_degree + in_degree
    laplacian = sp.diags(diagonal) - adjacency_matrix

    return laplacian
