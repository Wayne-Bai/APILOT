import networkx as nx

def has_eulerian_path(G, source=None):
    # Check if the graph is connected
    if not nx.is_connected(G):
        return False

    # A graph has an Eulerian path if at most two vertices have odd degree
    odd_degree_vertices = [v for v, d in G.degree() if d % 2 != 0]

    # If a source is specified, it must not have odd degree
    if source is not None and source in odd_degree_vertices:
        return False

    # If more than two vertices have odd degree, the graph cannot have an Eulerian path
    if len(odd_degree_vertices) > 2:
        return False

    # If exactly two vertices have odd degree, they must be the same vertex when considered as start and end of the path
    if len(odd_degree_vertices) == 2:
        return source is not None and odd_degree_vertices[0] == source and odd_degree_vertices[1] == source

    return True
