import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    # Check if G is an undirected graph and construct the adjacency matrix
    if not isinstance(G, nx.Graph):
        raise ValueError("'G' must be a NetworkX Graph instance.")

    if not nx.is_undirected(G):
        raise ValueError("'G' must be a directed graph for constructing the adjacency matrix.")

    # Construct the adjacency matrix using NetworkX's adjacency_matrix function
    adj_matrix = nx.adjacency_matrix(G).todense()

    # Convert the adjacency matrix attributes to a numpy array
    adj_matrix_np = adj_matrix.toarray()

    return adj_matrix_np
