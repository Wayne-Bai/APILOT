
from networkx import Graph

def compute_extreme_distance(G):
    # Initialize the extreme distance to 0
    extreme_distance = 0

    # Loop through all nodes in the graph
    for node in G.nodes:
        # Get the degree of the current node
        degree = G.degree[node]

        # If the degree is greater than the extreme distance, update it
        if degree > extreme_distance:
            extreme_distance = degree

    return extreme_distance
