import networkx as nx

def calculate_hits_authority_matrix(graph):
    # Ensure the graph is directed
    if not graph.is_directed():
        graph = graph.to_directed()
    
    # Calculate HITS scores
    hubs, authorities = nx.hits(graph)
    
    # Create the authority matrix
    authority_matrix = nx.to_numpy_array(graph, nodelist=sorted(graph.nodes()), weight=None)
    
    # Normalize authority scores
    authority_scores = [authorities[node] for node in sorted(graph.nodes())]
    authority_matrix = authority_matrix * authority_scores
    
    return authority_matrix

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 2)])
authority_matrix = calculate_hits_authority_matrix(G)
print(authority_matrix)
