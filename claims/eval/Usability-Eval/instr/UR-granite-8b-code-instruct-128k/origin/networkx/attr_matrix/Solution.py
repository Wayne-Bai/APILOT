import networkx as nx
import numpy as np

def get_adjacency_matrix(G):
    return nx.adjacency_matrix(G).toarray()
