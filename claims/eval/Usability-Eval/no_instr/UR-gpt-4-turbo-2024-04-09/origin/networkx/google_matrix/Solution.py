import networkx as nx

def create_google_matrix(graph, alpha=0.85):
    # Compute the Google matrix using networkx's google_matrix function
    G_matrix = nx.google_matrix(graph, alpha=alpha)
    return G_matrix
