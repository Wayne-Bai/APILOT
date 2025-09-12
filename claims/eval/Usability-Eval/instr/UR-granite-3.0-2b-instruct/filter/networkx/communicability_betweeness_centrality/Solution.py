import networkx as nx

def subgraph_communicability(G):
    # Calculate the adjacency matrix of the graph
    adj_matrix = nx.to_numpy_array(G)

    # Calculate the communicability matrix
    comms = nx.communicability(G)

    # Calculate the subgraph communicability for all pairs of nodes
    subgraph_comms = nx.subgraph_communicability(G, adj_matrix)

    return subgraph_comms
