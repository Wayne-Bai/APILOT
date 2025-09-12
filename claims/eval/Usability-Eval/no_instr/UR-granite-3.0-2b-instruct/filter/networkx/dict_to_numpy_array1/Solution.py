import numpy as np
import networkx as nx

def dict_to_1d_numpy(dictionary):
    # Create a graph from the dictionary
    G = nx.from_dict_of_lists(dictionary, create_using=nx.Graph())

    # Get the nodes of the graph
    nodes = list(G.nodes)

    # Convert the dictionary of nodes to a 1d numpy array
    numpy_array = np.array(list(dictionary.values()))

    return numpy_array, nodes
