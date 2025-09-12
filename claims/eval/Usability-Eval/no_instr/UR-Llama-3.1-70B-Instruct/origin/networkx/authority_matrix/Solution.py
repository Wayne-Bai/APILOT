import networkx as nx
import numpy as np

def hits_authority(G):
    """
    Compute HITS authority scores for nodes in a graph.

    Parameters
    ----------
    G : NetworkX graph
        A NetworkX graph.

    Returns
    -------
    A : dictionary
        Dictionary of nodes with authority scores as the value.
    """
    # HITS algorithm parameters
    max_iterations = 100
    tolerance = 1.0e-08

    # initializes the hub and authority matrices
    hubs, authorities = {}, {}
    for node in G.nodes():
        hubs[node] = 1
        authorities[node] = 1

    # performs the algorithm iterations
    for _ in range(max_iterations):
        last_AUTHORITIES = authorities
        authorities = {}
        for node in G.nodes():
            authorities[node] = sum(hubs[neighbor] for neighbor in G[node])
        
        last_HUBS = hubs
        hubs = {}
        for node in G.nodes():
            hubs[node] = sum(authorities[neighbor] for neighbor in G[node])
        
        # Check convergence
        if (_!= 0) and (np.allclose(authorities.values(), last_AUTHORITIES.values(), atol=tolerance) and
                         np.allclose(hubs.values(), last_HUBS.values(), atol=tolerance)):
            break

    return authorities

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.DiGraph()
    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('A', 'C'),
        ('C', 'A'),
        ('B', 'D'),
        ('D', 'B')
    ]
    G.add_edges_from(edges)

    # Calculate HITS authority scores
    hits_authorities = hits_authority(G)
    
    print("HITS Authority scores:")
    for node, score in hits_authorities.items():
        print(f"{node}: {score}")
