import networkx as nx

def minimum_weight_maximal_matching(G):
    # Create a copy of the graph to work with
    G_copy = G.copy()
    
    # Initialize the matching set
    matching = set()
    
    # Sort edges by weight in ascending order
    edges = sorted(G_copy.edges(data=True), key=lambda x: x[2].get('weight', 1))
    
    # Iterate over the sorted edges
    for u, v, data in edges:
        # If neither u nor v are in the current matching, add the edge to the matching
        if u not in matching and v not in matching:
            matching.add(u)
            matching.add(v)
            matching.add((u, v))
    
    # Convert the matching set to a list of edges
    matching_edges = [(u, v) for u, v in matching if isinstance(u, tuple)]
    
    return matching_edges

# Example usage:
G = nx.Graph()
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 1, weight=4)

matching = minimum_weight_maximal_matching(G)
print("Minimum-weight maximal matching:", matching)
