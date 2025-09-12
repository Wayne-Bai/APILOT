
import networkx as nx
import numpy as np

def get_numpy_array(G):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    If only G is passed in, then the adjacency matrix is constructed.
    """
    return np.array(nx.to_numpy_matrix(G))
