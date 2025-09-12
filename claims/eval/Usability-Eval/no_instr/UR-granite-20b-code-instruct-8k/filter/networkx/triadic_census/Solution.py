import networkx as nx

def triadic_census(G):
    """
    Determines the triadic census of a directed graph.

    The triadic census is a count of how many of the 16 possible types of triads
    are present in a directed graph.

    Parameters
    ----------
    G : NetworkX DiGraph
        A directed graph.

    Returns
    -------
    census : dict
        A dictionary with keys being the triad types and values being the count of triads of that type.

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4), (4, 5)])
    >>> triadic_census(G)
    {'003': 1, '012': 2, '021D': 1, '021U': 1, '021C': 1, '102': 1, '111D': 1, '111U': 1, '111C': 1}
    """
    census = {}
    for triad in nx.triads(G):
        t = ''.join(sorted(str(triad)))
        if t not in census:
            census[t] = 0
        census[t] += 1
    return census
