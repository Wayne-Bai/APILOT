import networkx as nx

# Define the function to compute the coverage of a partition
def coverage(G, part):
    # Get the number of nodes in the graph
    num_nodes = len(G)
    
    # Get the number of edges in the graph
    num_edges = sum([d.get('weight', 1) for u, v, d in G.edges(data=True)])
    
    # Get the number of intra-community edges
    num_intra_edges = 0
    for node in part:
        neighbors = set(G.neighbors(node)) & set(part)
        num_intra_edges += len(neighbors)
    
    # Compute the coverage
    coverage = num_intra_edges / (num_nodes * (num_nodes - 1) / 2)
    
    return coverage
