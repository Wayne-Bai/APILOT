import networkx as nx
import numpy as np

def attribute_mixing_matrix(G, attribute):
    """
    Returns the mixing matrix for the given attribute.

    Parameters:
    G (networkx.Graph): The input graph.
    attribute (str): The attribute to calculate the mixing matrix for.

    Returns:
    np.ndarray: The mixing matrix.
    """
    # Get the unique attribute values
    values = set(nx.get_node_attributes(G, attribute).values())
    
    # Initialize the mixing matrix
    mixing_matrix = np.zeros((len(values), len(values)))
    
    # Iterate over the edges in the graph
    for u, v in G.edges():
        # Get the attribute values of the nodes
        u_attr = G.nodes[u][attribute]
        v_attr = G.nodes[v][attribute]
        
        # Get the indices of the attribute values
        i = list(values).index(u_attr)
        j = list(values).index(v_attr)
        
        # Increment the corresponding entry in the mixing matrix
        mixing_matrix[i, j] += 1
    
    # Normalize the mixing matrix
    row_sums = mixing_matrix.sum(axis=1)
    mixing_matrix = mixing_matrix / row_sums[:, np.newaxis]
    
    return mixing_matrix

# Example usage:
G = nx.Graph()
G.add_node(1, attribute='A')
G.add_node(2, attribute='B')
G.add_node(3, attribute='A')
G.add_node(4, attribute='B')
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

mixing_matrix = attribute_mixing_matrix(G, 'attribute')
print(mixing_matrix)
