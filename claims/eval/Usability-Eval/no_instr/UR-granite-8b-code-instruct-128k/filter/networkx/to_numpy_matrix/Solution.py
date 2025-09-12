import networkx as nx
def get_adjacency_matrix(graph):
    adjacency_matrix = nx.to_numpy_matrix(graph)
    return adjacency_matrix
