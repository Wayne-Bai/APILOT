import networkx as nx

def has_eulerian_path(G, source=None):
    # Count the number of nodes with odd degree
    odd_degree_nodes = [node for node in G.nodes() if G.degree(node) % 2 == 1]
    
    # For an undirected graph to have an Eulerian path:
    # - it can have either 0 or 2 nodes of odd degree
    if len(odd_degree_nodes) not in [0, 2]:
        return False
    
    # If source is specified, it must be one of the odd degree nodes if there are exactly 2
    if source is not None and len(odd_degree_nodes) == 2 and source not in odd_degree_nodes:
        return False
    
    # Ensure the graph is connected (check connected component for non-isolated nodes)
    if len(G.nodes()) == 0:
        return False
    
    # Find the connected component containing the source (if specified)
    component_nodes = G.nodes() if source is None else nx.node_connected_component(G, source)
    
    # Ensure all nodes with edges are in the connected component
    for node in G.nodes():
        if G.degree(node) > 0 and node not in component_nodes:
            return False
    
    return True
