import networkx as nx

def has_eulerian_path(G, source=None):
    """
    Return True iff G has an Eulerian path.
    An Eulerian path is a path in a graph which uses each edge of a graph exactly once.
    If source is specified, then this function checks whether an Eulerian path that starts at node source exists.

    Parameters
    ----------
    G : NetworkX graph
    source : node, optional
    """
    # find all nodes with odd degree
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2!= 0]

    # if more than two nodes have odd degree, an Eulerian path does not exist
    if len(odd_degree_nodes) > 2:
        return False

    # find strongly connected components in the graph
    scc = list(nx.strongly_connected_components(G))

    # if there is more than one strongly connected component, an Eulerian path does not exist
    if len(scc) > 1:
        return False

    # if a source node is specified, check that it has odd degree
    if source is not None and (source not in odd_degree_nodes or len(odd_degree_nodes) > 1):
        return False

    # if a source node is specified, check that it is in the same strongly connected component as the other nodes with odd degree
    if source is not None:
        source_component = None
        for component in scc:
            if source in component:
                source_component = component
                break
        if not all(node in source_component for node in odd_degree_nodes):
            return False

    return True

# example usage:
if __name__ == "__main__":
    G = nx.Graph([(1, 2), (2, 3), (1, 3), (3, 4), (4, 1)])
    print(has_eulerian_path(G))  # prints: True

    G = nx.Graph([(1, 2), (2, 3), (1, 3), (3, 4), (4, 1), (1, 5)])
    print(has_eulerian_path(G))  # prints: False
