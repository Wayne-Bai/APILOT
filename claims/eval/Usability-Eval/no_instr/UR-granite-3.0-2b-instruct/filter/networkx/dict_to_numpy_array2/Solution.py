import numpy as np
import networkx as nx

def dict_of_dicts_to_2d_numpy(d, mapping=None):
    # Create a NetworkX graph from the dictionary of dictionaries
    G = nx.from_dict_of_lists(d, create_using=nx.Graph(), defaultdict=dict)

    # If a mapping is provided, update the graph with the mapping
    if mapping is not None:
        G = nx.relabel.relabel_nodes(G, mapping)

    # Convert the graph to a 2D numpy array
    arr = nx.to_numpy(G, dtype=int)

    return arr
