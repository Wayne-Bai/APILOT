import networkx as nx

def has_eulerian_path(G):
    """
    This function checks if a graph `G` has an Eulerian path.
    An Eulerian path is a path in a graph which uses each edge of a graph exactly once.
    """
    return nx.has_eulerian_path(G)
