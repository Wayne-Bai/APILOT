import networkx as nx

def triadic_census_of_subgraph(G, nodelist=None):
    if nodelist is not None:
        # Create subgraph from nodelist
        H = G.subgraph(nodelist)
    else:
        H = G  # use the whole graph if no nodelist is provided
    
    # Calculate the triadic census for the (sub)graph
    triadic_census = nx.triadic_census(H)
    return triadic_census

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 1)])

# Calculate triadic census for the entire graph
print(triadic_census_of_subgraph(G))

# Calculate triadic census for a subset of nodes
print(triadic_census_of_subgraph(G, nodelist=[1, 2, 3]))
