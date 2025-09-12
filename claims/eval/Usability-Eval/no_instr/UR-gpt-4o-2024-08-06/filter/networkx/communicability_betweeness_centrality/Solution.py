import networkx as nx

def subgraph_communicability(G):
    """
    Returns the subgraph communicability for all pairs of nodes in G.
    
    Subgraph communicability is calculated using the adjacency matrix of G.
    Parameters:
    G : Graph
        A NetworkX graph.
        
    Returns:
    C : dict
        Dictionary of dictionaries containing communicability between all pairs of nodes. 
    """
    A = nx.adjacency_matrix(G).todense()
    expA = np.exp(A)  # Use matrix exponential

    n = len(G)
    communicability = {}

    # Generate communicability for each pair of nodes
    for i in range(n):
        for j in range(n):
            node_i = list(G.nodes)[i]
            node_j = list(G.nodes)[j]
            
            if node_i not in communicability:
                communicability[node_i] = {}
            
            # Extract communicability value
            communicability[node_i][node_j] = expA[i, j]
            
    return communicability

# Example usage:
G = nx.complete_graph(4)
comm = subgraph_communicability(G)
print(comm)
