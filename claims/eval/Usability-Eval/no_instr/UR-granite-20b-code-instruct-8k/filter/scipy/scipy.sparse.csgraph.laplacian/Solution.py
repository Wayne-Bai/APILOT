import numpy as np
import scipy.sparse as sp

def directed_laplacian(graph):
    """
    Return the Laplacian of a directed graph.
    
    Parameters
    ----------
    graph : scipy.sparse matrix
        The adjacency matrix of the graph.
    
    Returns
    -------
    L : scipy.sparse matrix
        The Laplacian of the graph.
    """
    D = sp.diags(np.sum(graph, axis=1).flat)
    L = D - graph
    return L
