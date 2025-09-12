import networkx as nx

def has_eulerian_path(G, source=None):
    """
    Check if G has an Eulerian path.
    An Eulerian path is a path in a graph which uses each edge of a graph exactly once.
    If source is specified, then this function checks whether an Eulerian path that starts
    at node source exists.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
        Specify starting node for search.

    Returns
    -------
    has_path : bool
        True if an Eulerian path exists, False otherwise.

    Raises
    ------
    NetworkXError
        If the graph is not directed or is empty.

    Examples
    --------
    To test whether a graph has an Eulerian path, you can use the function like this ::

        >>> G = nx.DiGraph()
        >>> G.add_edge('a', 'b')
        >>> G.add_edge('a', 'c')
        >>> G.add_edge('b', 'c')
        >>> nx.has_eulerian_path(G)
        True
        >>> G = nx.DiGraph()
        >>> G.add_edge('a', 'b')
        >>> G.add_edge('b', 'c')
        >>> nx.has_eulerian_path(G)
        False

    """
    if not G or len(G) == 0:
        raise nx.NetworkXError("Input graph is not directed or is empty.")

    if source is None:
        # If source is None, find any vertex with in degree equal to out degree
        for node in G:
            if G.in_degree(node) == G.out_degree(node):
                source = node
                break
        else:
            return False
    if not nx.is_connected(G):
        return False
    if G.in_degree(source) != G.out_degree(source):
        return False

    return True
