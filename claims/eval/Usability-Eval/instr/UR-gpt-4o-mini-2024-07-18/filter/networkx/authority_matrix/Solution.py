import networkx as nx

def get_hits_authority_matrix(graph):
    # Compute HITS scores
    hubs, authorities = nx.hits(graph, normalized=True)
    
    # Create authority matrix
    authority_matrix = {node: auth for node, auth in authorities.items()}
    
    return authority_matrix

# Example usage
if __name__ == "__main__":
    # Create a sample directed graph
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])

    # Get the HITS authority matrix
    authority_matrix = get_hits_authority_matrix(G)
    print("Authority Matrix:", authority_matrix)
