import networkx as nx

def get_mixing_matrix(G, attribute):
    """
    Returns the mixing matrix for a given attribute in the graph.
    
    Parameters:
    G: NetworkX graph
       The graph on which to analyze the attribute.
       
    attribute: str
       The name of the node attribute to consider.

    Returns:
    dict: A dictionary representing the mixing matrix.
    """
    # Initialize an empty dictionary to hold the mixing matrix
    mixing_matrix = {}
    
    # Iterate over all edges in the graph
    for u, v in G.edges():
        # Get the attribute values for the connected nodes
        attr_u = G.nodes[u].get(attribute)
        attr_v = G.nodes[v].get(attribute)
        
        # Ensure that both nodes have the attribute
        if attr_u is not None and attr_v is not None:
            if attr_u not in mixing_matrix:
                mixing_matrix[attr_u] = {}
            if attr_v not in mixing_matrix[attr_u]:
                mixing_matrix[attr_u][attr_v] = 0

            # Increase the count for the attribute pair (attr_u, attr_v)
            mixing_matrix[attr_u][attr_v] += 1
    
    return mixing_matrix

# Example usage
# Create a graph and assign attributes to nodes
G = nx.Graph()
G.add_nodes_from([
    (1, {"color": "red"}), 
    (2, {"color": "blue"}), 
    (3, {"color": "red"}), 
    (4, {"color": "blue"}), 
    (5, {"color": "red"})
])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])

# Get the mixing matrix for the 'color' attribute
mixing_matrix = get_mixing_matrix(G, "color")
print(mixing_matrix)
