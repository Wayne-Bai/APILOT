import networkx as nx

def compute_communicability(G):
    """
    Computes the communicability for all pairs of nodes in the graph G.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    dict: A dictionary where keys are node pairs and values are their communicability scores.
    """
    communicability_dict = {}
    
    # Calculate communicability for all pairs
    for u in G.nodes():
        for v in G.nodes():
            if u != v:  # Avoid self-communication
                # Use the exponential of the adjacency matrix normalized
                comm_score = nx.communicability(G, nodes=[u, v]).get(u, {}).get(v, 0)
                communicability_dict[(u, v)] = comm_score
                
    return communicability_dict

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])
# result = compute_communicability(G)
# print(result)
