import networkx as nx

def authority_matrix(G):
    A = nx.hits(G)
    return A
