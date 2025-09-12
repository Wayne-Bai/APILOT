import networkx as nx

def minimum_weight_maximal_matching(G):
    # Create a copy of the graph to work with
    G_copy = G.copy()
    
    # Initialize the matching
    matching = []
    
    # Sort edges by weight in ascending order
    edges = sorted(G_copy.edges(data=True), key=lambda x: x[2].get('weight', 1))
    
    # Iterate over the sorted edges
    for u, v, data in edges:
        # If neither u nor v are in the current matching, add the edge to the matching
        if not any(u in pair or v in pair for pair in matching):
            matching.append((u, v))
            # Remove the nodes u and v from the graph to ensure maximality
            G_copy.remove_node(u)
            G_copy.remove_node(v)
    
    return matching

# Example usage:
G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 5), (2, 3, 1), (3, 4, 2), (4, 1, 3)])
matching = minimum_weight_maximal_matching(G)
print("Minimum-weight maximal matching:", matching)
