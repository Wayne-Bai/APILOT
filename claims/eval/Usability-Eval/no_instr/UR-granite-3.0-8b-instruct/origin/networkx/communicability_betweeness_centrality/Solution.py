import networkx as nx

def subgraph_communicability(G):
    # Calculate communicability matrix
    comm_matrix = nx.communicability_exp(G)

    # Create a dictionary to store communicability for all pairs of nodes
    communicability = {tuple(sorted(node_pair)): comm_matrix[node_pair] for node_pair in comm_matrix}

    return communicability
