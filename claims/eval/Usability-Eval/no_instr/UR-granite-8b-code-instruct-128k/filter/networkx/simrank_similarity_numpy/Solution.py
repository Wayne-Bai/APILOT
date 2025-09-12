
import networkx as nx
import numpy as np

def simrank(G, k=10):
    A = nx.to_numpy_matrix(G)
    S = np.zeros((A.shape[0], A.shape[0]))

    for i in range(k):
        S = (S + S @ A @ S) / 2

    return S
