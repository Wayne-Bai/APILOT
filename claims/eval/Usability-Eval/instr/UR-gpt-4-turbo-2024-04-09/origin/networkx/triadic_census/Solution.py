import networkx as nx

def triadic_census(G, nodelist=None):
    if nodelist is not None:
        # Create a subgraph containing only the nodes in nodelist
        subgraph = G.subgraph(nodelist)
        return nx.algorithms.triads.triadic_census(subgraph)
    else:
        # Calculate triadic census for the entire graph
        return nx.algorithms.triads.triadic_census(G)

# Example usage:
# Creating a directed graph
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3)])

# Compute triadic census for the entire graph
print(triadic_census(DG))

# Compute triadic census for a subset of nodes
print(triadic_census(DG, nodelist=[1, 2, 3]))
