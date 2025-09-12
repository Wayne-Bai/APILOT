import networkx as nx

def quotient_graph(G, relation):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters
    ----------
    G : NetworkX graph
        The graph for which the quotient graph is to be computed.
    relation : callable
        A function that takes two nodes as input and returns a boolean value indicating whether the nodes are related.

    Returns
    -------
    H : NetworkX graph
        The quotient graph of G under the specified equivalence relation on nodes.
    """
    # Create a new graph with the same node set as G
    H = nx.Graph(G)

    # Add edges between related nodes in G
    for u, v in G.edges():
        if relation(u, v):
            H.add_edge(u, v)

    return H
