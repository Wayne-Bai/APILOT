import numpy as np
import networkx as nx

def dict_to_numpy_array(d, mapping=None):
    # Create a graph from the dictionary
    G = nx.fromDict(d, create_using=nx.Graph())

    # If a mapping is provided, apply it to the nodes
    if mapping:
        G = nx.relabel_nodes(G, mapping)

    # Convert the graph to a 1D numpy array
    array = np.array(list(G.nodes()))

    return array
