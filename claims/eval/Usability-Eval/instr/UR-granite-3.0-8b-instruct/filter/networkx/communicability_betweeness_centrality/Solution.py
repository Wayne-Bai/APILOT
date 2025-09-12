import networkx as nx

def subgraph_communicability(G):
    communicability = nx.communication_matrix(G)
    return communicability
