import networkx as nx

def return_small_undirected_graph():
    """
    Returns a small undirected graph described by graph_description.
    """
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
    return graph
