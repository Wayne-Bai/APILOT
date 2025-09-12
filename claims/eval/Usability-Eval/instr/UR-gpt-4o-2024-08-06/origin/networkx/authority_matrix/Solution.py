import networkx as nx

def hits_authority_matrix(G):
    # Compute HITS hubs and authorities scores
    hubs, authorities = nx.hits(G)

    # Create an authority matrix from the authority scores
    authority_matrix = nx.to_numpy_array(G, nodelist=sorted(G.nodes()), dtype=float)

    # Replace matrix entries with the authority values
    for i, node in enumerate(sorted(G.nodes())):
        authority_matrix[i, i] = authorities[node]
    
    return authority_matrix

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (3, 2)])

authority_matrix = hits_authority_matrix(G)
print("Authority Matrix:")
print(authority_matrix)
