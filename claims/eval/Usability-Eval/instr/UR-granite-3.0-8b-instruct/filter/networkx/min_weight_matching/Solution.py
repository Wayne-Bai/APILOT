import networkx as nx

def minimum_weight_maximal_matching(G):
    # Create a copy of the graph
    G_copy = G.copy()

    # Initialize an empty matching
    matching = {}

    # Iterate over the edges in the graph
    for u, v, weight in G_copy.edges(data=True):
        # If the edge is not already in the matching
        if (u, v) not in matching and (v, u) not in matching:
            # Add the edge to the matching
            matching[(u, v)] = weight

    return matching
