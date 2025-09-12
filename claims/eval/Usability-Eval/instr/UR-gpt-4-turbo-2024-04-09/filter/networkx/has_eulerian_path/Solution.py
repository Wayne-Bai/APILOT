import networkx as nx

def has_eulerian_path(G, source=None):
    # Check if the graph is empty
    if len(G) == 0:
        return True

    # Compute the degree of each node
    degree_counts = dict(G.degree())
    
    # Count nodes with odd degree
    odd_degree_nodes = [node for node, degree in degree_counts.items() if degree % 2 != 0]

    # Check for Eulerian path conditions
    if len(odd_degree_nodes) not in [0, 2]:
        return False
    if len(odd_degree_nodes) == 0:
        return True
    
    if source is not None:
        # If source is specified and it's not one of the nodes with odd degree, return False
        if source not in odd_degree_nodes:
            return False
        # Ensure connectivity from the source
        G_un = G.to_undirected() if G.is_directed() else G
        return nx.is_connected(G_un)
    
    # If source is not specified, check for Eulerian path any starting from any node with odd degree
    if source is None:
        if len(odd_degree_nodes) == 2:
            # Check if the graph is connected
            G_un = G.to_undirected() if G.is_directed() else G
            return nx.is_connected(G_un)
    
    return False
