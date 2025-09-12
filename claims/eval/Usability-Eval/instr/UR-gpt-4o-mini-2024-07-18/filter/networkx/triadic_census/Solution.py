import networkx as nx
from itertools import combinations

def directed_triad_census(G, nodelist=None):
    if nodelist is not None:
        G = G.subgraph(nodelist)
    
    triad_types = {i: 0 for i in range(16)}
    
    for u, v, w in combinations(G.nodes(), 3):
        edges = G.has_edges_from([(u, v), (u, w), (v, u), (v, w), (w, u), (w, v)])

        # Create a bitmask based on the presence of directed edges
        bitmask = (edges[0] << 5) | (edges[1] << 4) | (edges[2] << 3) | \
                  (edges[3] << 2) | (edges[4] << 1) | edges[5]

        triad_types[bitmask] += 1

    return triad_types

# Example of how to use the function
# G = nx.DiGraph()  # Create a directed graph
# Add edges to G
# census = directed_triad_census(G)
