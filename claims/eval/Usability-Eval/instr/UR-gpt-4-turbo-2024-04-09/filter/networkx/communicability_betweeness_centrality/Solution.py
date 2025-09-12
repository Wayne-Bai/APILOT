import networkx as nx

def subgraph_communicability(G):
    return nx.communicability_exp(G)
