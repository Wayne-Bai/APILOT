import networkx as nx

def has_eulerian_path(G, source=None):
    """Return True iff G has an Eulerian path.
    
    An Eulerian path is a path in a graph which uses each edge of a graph exactly once. If source is specified, then this function checks whether an Eulerian path that starts at node source exists.
    
    Parameters:
        G (networkx.Graph): The graph to check for an Eulerian path.
        source (str or None): The source node of the Eulerian path, if it exists. If None, then any valid source node will be used.
    
    Returns:
        bool: True iff G has an Eulerian path.
    """
    # Check if G is a connected graph
    if not nx.is_connected(G):
        return False
    
    # Check if every vertex in G has even degree
    for vertex in G.nodes():
        if vertex.degree % 2 == 1:
            return False
    
    # Check if G has an Eulerian cycle (i.e., a Hamiltonian path that starts and ends at the same node)
    if nx.has_eulerian_cycle(G):
        return True
    
    # If G is not connected, then it cannot have an Eulerian path
    if not source:
        return False
    
    # Check if there is a valid Eulerian path starting at source
    for edge in G.edges():
        if edge.source == source and edge.target not in G[source]:
            return True
    
    return False
