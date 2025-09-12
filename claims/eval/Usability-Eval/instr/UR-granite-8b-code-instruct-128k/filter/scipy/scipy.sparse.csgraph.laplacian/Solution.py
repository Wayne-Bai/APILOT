import scipy.sparse as sparse

def get_laplacian(graph):
    """
    Returns the Laplacian of a directed graph.
    
    Parameters:
    graph (scipy.sparse.csr_matrix): The directed graph as a sparse matrix in CSR format.
    
    Returns:
    scipy.sparse.csr_matrix: The Laplacian of the graph.
    """
    degree = graph.sum(axis=1)
    degree = sparse.diags(degree.flatten(), [0])
    laplacian = degree - graph
    
    return laplacian
