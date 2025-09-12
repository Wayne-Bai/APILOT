import networkx as nx

def has_eulerian_path(G, source=None):
    # For a graph to have an Eulerian path:
    # - At most one vertex can have (out_degree - in_degree) = 1, this will be the starting vertex
    # - At most one vertex can have (in_degree - out_degree) = 1, this will be the ending vertex
    # - All other vertices should have equal in_degree and out_degree, i.e., (out_degree - in_degree) = 0

    if not nx.is_connected(G.to_undirected()):
        return False

    odd_degree_count = 0
    start_nodes = 0
    end_nodes = 0

    for node in G.nodes():
        out_degree = G.out_degree(node)
        in_degree = G.in_degree(node)
        degree_difference = out_degree - in_degree

        if degree_difference == 1:
            start_nodes += 1
        elif degree_difference == -1:
            end_nodes += 1
        elif degree_difference != 0:
            odd_degree_count += 1

    if source is not None:
        # If a specific starting source is given, check if it's suitable for starting
        out_degree = G.out_degree(source)
        in_degree = G.in_degree(source)
        if out_degree - in_degree != 1:
            return False

    # Check suitable conditions for Eulerian path
    if (start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0):
        return True

    return False

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(0, 1), (1, 2), (2, 3)])
# print(has_eulerian_path(G, source=0))
