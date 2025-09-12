import networkx as nx
import numpy as np

def attribute_matrix(G, attr_to_use=None):
    """
    Returns the attribute matrix using attributes from G as a numpy array.

    If only G is passed in, then the adjacency matrix is constructed.

    Parameters:
    G (Networkx graph): Input graph
    attr_to_use (list): List of attributes to use (default is all)

    Returns:
    arr (numpy array): Attribute matrix
    """

    # If no attributes are specified, use all attributes of G
    if attr_to_use is None:
        attr_to_use = G.node.keys()

    # Initialize attribute matrix
    A = np.zeros((G.number_of_nodes(), len(attr_to_use)))

    # Populate attribute matrix
    for i, node in enumerate(G.nodes):
        for j, attr in enumerate(attr_to_use):
            A[i, j] = G.nodes[node].get(attr, 0)  # Use get to avoid KeyError

    return A

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])
G.nodes[1]['color'] ='red'
G.nodes[2]['color'] = 'blue'
G.nodes[3]['shape'] = 'circle'
G.nodes[1]['size'] = 10
G.nodes[2]['size'] = 20
G.nodes[3]['size'] = 30

print(attribute_matrix(G, ['color','size']))
