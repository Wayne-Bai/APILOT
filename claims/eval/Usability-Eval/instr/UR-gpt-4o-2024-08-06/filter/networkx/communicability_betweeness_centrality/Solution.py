import networkx as nx

def subgraph_communicability(G):
    """
    Returns subgraph communicability for all pairs of nodes in graph G.

    Parameters:
    G : NetworkX graph
        The graph for which to calculate subgraph communicability.

    Returns:
    dict : A dictionary with node pairs as keys and their subgraph communicability as values.
    """
    communicability = {}
    for u in G.nodes():
        for v in G.nodes():
            if u == v:
                continue
            # Calculate the subgraph communicability for the pair (u, v)
            subgraph_G = G.subgraph(set(G.nodes()) - {u, v})
            num_paths_uv = sum(1 for path in nx.all_simple_paths(G, u, v))
            num_paths_complement = sum(1 for path in nx.all_simple_paths(subgraph_G, u, v))
            
            communicability[(u, v)] = num_paths_uv - num_paths_complement
    
    return communicability

# Example usage
G = nx.erdos_renyi_graph(5, 0.5)
communicability = subgraph_communicability(G)
print(communicability)
