import networkx as nx

def get_attribute_matrix(G):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    If only G is passed in, then the adjacency matrix is constructed.

    Parameters
    ----------
    G : graph

    Returns
    -------
    A : numpy array

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=0.5)
    >>> G.add_node(3, color='blue')
    >>> get_attribute_matrix(G)
    array([[ 0.,  0.5,  0. ],
           [ 0.5,  0.,  0. ],
           [ 0.,  0.,  0. ]])

    """
    A = nx.to_numpy_array(G)
    return A