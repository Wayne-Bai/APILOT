import networkx as nx

def performance(G, partition):
    # Calculate the number of intra-community edges
    intra_edges = 0
    for (u, v) in G.edges():
        if u in partition and v in partition:
            intra_edges += 1
    
    # Calculate the number of inter-community non-edges
    inter_non_edges = 0
    for (u, v) in G.edges():
        if not (u in partition and v in partition):
            inter_non_edges += 1
    
    # Calculate the total number of potential edges
    total_potential_edges = len(G.nodes()) * (len(G.nodes()) - 1) / 2
    
    return (intra_edges + inter_non_edges) / total_potential_edges
