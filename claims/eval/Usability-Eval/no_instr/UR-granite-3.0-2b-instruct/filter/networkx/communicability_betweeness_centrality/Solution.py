import networkx as nx

def subgraph_communicability(G):
    # Calculate adjacency matrix
    adj_matrix = nx.to_numpy_array(G)

    # Calculate subgraph communicability
    communicability = nx.communicability.subgraph_communicability(G, adj_matrix)

    return communicability
