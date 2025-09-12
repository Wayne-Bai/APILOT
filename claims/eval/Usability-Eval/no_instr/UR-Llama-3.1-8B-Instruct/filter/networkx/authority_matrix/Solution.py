import networkx as nx

def return_hits_authority_matrix(graph):
    """
    This function returns the HITS authority matrix of a given graph.
    
    Parameters:
    graph (networkx.Graph or networkx.DiGraph): The input graph.
    
    Returns:
    dict: A dictionary where the keys are the nodes in the graph and the values are
          the authority scores for each node.
    """
    
    # Calculate the HITS authority scores using NetworkX's hits() function
    hits = nx.hits(graph)
    
    # The hits() function returns a tuple, where the first element is the authority scores and the second is the hub scores
    # We're interested in the authority scores, so we use the first element of the tuple
    authority_scores = hits[0]
    
    return authority_scores

# Example usage
if __name__ == "__main__":
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add some nodes and edges to the graph
    G.add_edge('A', 'B')
    G.add_edge('B', 'C')
    G.add_edge('C', 'D')
    G.add_edge('D', 'E')
    
    # Get the HITS authority matrix
    authority_matrix = return_hits_authority_matrix(G)
    
    # Print the authority scores
    print(authority_matrix)
