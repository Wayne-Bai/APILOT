py
import networkx as nx

def generate_adjacency_matrix(graph):
    """
    Generate adjacency matrix of graph G.

    Parameters
    ----------
    graph : NetworkX graph
        A graph to be converted to an adjacency matrix.

    Returns
    -------
    adj_matrix : numpy.ndarray
        The adjacency matrix of the graph G.

    """
    adj_matrix = nx.to_numpy_array(graph)
    return adj_matrix
