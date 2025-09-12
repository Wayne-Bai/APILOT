import networkx as nx
import numpy as np

def dict_to_numpy_array(dict_of_dicts, mapping=None):
    # Create an empty graph
    G = nx.DiGraph()

    # Add nodes and edges based on the dictionary
    for node, edges in dict_of_dicts.items():
        G.add_node(node)
        for edge, weight in edges.items():
            G.add_edge(node, edge, weight=weight)

    # Convert the graph to a 2D numpy array with optional mapping
    if mapping is None:
        return np.array(nx.to_numpy_array(G))
    else:
        return np.array([[mapping[u], mapping[v], G.get_edge_data(u, v)['weight']] for u, v in G.edges()])
