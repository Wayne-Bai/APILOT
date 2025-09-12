import networkx as nx

def return_graph_adjacency_matrix(graph):
    adj_matrix = nx.adj_matrix(graph)
    return adj_matrix.tocsr()
