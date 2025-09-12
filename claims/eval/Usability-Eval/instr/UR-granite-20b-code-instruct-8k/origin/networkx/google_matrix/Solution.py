import networkx as nx

def google_matrix(graph):
    eigenvalues, eigenvectors = nx.google_matrix(graph)
    return eigenvalues, eigenvectors
