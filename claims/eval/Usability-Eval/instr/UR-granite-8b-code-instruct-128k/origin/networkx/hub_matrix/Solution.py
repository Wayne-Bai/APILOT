import networkx as nx

def hits_hub_matrix(graph):
    hub_matrix = nx.hits_hub_matrix(graph)
    return hub_matrix
