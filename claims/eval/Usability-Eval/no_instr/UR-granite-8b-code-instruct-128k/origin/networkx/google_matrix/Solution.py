import networkx as nx

def generate_google_matrix(graph):
    google_matrix = nx.google_matrix(graph)
    return google_matrix
