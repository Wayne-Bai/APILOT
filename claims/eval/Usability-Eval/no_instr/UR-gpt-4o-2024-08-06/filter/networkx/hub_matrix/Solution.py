import networkx as nx
import numpy as np

def compute_hits_hub_matrix(G):
    # Compute HITS algorithm
    hubs, _ = nx.hits(G, normalized=True)
    
    # Extract nodes and their hub scores
    nodes = list(G.nodes())
    hub_scores = [hubs[node] for node in nodes]
    
    # Create and return the hub matrix
    hub_matrix = np.diag(hub_scores)
    
    return hub_matrix

# Example usage:
if __name__ == "__main__":
    # Create a sample directed graph
    G = nx.DiGraph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
    
    # Get the HITS hub matrix
    hub_matrix = compute_hits_hub_matrix(G)
    print("HITS Hub Matrix:")
    print(hub_matrix)
