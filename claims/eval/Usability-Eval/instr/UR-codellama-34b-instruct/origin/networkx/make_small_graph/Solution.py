import networkx as nx

def get_small_graph(graph_description):
    """
    Returns a small graph based on the given description.
    The description should be in the form of a list of edges, where each edge is a tuple of two integers.
    For example: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    """
    G = nx.Graph()
    for edge in graph_description:
        G.add_edge(*edge)
    return G
