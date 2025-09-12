
import networkx as nx
import numpy as np

def get_attribute_matrix(G):
    return np.array(nx.to_numpy_matrix(G, attribute='attribute'))
