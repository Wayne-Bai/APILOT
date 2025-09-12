import networkx as nx

def hits_authority_matrix(G):
    # Perform the HITS algorithm
    _, authorities = nx.hits(G)
    
    # Prepare the authority matrix
    nodes = list(G.nodes())
    n = len(nodes)
    authority_matrix = [[0]*n for _ in range(n)]
    
    node_index = {node: i for i, node in enumerate(nodes)}

    for node, authority_score in authorities.items():
        i = node_index[node]
        authority_matrix[i][i] = authority_score

    return authority_matrix

# Example usage
G = nx.path_graph(4)  # Creating a path graph with 4 nodes
authority_matrix = hits_authority_matrix(G)
print(authority_matrix)
