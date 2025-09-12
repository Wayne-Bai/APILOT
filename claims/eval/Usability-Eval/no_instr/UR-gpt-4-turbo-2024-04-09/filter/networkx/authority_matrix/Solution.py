import networkx as nx

def hits_authority_matrix(G):
    # Initialize the HITS algorithm on a given graph G
    _, authorities = nx.hits(G)
    
    # Convert authorities dictionary to a matrix
    nodes = list(G.nodes())
    authority_matrix = [[authorities[node2] if node == node2 else 0 for node2 in nodes] for node in nodes]
    
    return authority_matrix

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])
authority_matrix = hits_authority_matrix(G)
for row in authority_matrix:
    print(row)
