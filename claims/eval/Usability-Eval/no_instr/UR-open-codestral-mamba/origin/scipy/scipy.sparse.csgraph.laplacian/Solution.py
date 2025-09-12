import scipy.sparse as sp
import numpy as np

def calculate_laplacian(graph):
    # Check if the graph is a scipy.sparse matrix
    if not sp.issparse(graph):
        raise ValueError("Input graph must be a sparse matrix.")

    # Calculate the degree of each node
    degree = np.sum(graph, axis=1)

    # Calculate the Laplacian matrix
    laplacian = sp.diags(degree, dtype=graph.dtype) - graph

    return laplacian
