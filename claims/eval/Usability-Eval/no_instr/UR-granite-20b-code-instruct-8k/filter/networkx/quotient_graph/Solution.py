import networkx as nx

def quotient_graph(G, nodes):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.
    """
    quotient_edges = [(nodes[u], nodes[v]) for u, v in G.edges()]
    return nx.Graph(quotient_edges)
