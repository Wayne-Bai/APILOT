import networkx as nx
import numpy as np

def get_attribute_matrix(G, attribute=None):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    If no attribute is specified, the adjacency matrix is returned.

    Parameters:
    - G: A networkx graph
    - attribute: The node attribute to use for constructing the matrix

    Returns:
    - A numpy array representation of the graph data
    """
    if attribute is None:
        # Return the adjacency matrix as a numpy array
        return nx.to_numpy_array(G)

    # Extract the attribute for each node
    nodelist = list(G.nodes)
    n = len(nodelist)
    attribute_matrix = np.zeros((n, n))

    for i, u in enumerate(nodelist):
        for j, v in enumerate(nodelist):
            # Check if the edge exists and if it has the attribute
            if G.has_edge(u, v) and attribute in G[u][v]:
                attribute_matrix[i, j] = G[u][v][attribute]
            else:
                # If there's no attribute or no edge, set to zero
                attribute_matrix[i, j] = 0

    return attribute_matrix

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edge(1, 2, weight=4.2)
G.add_edge(2, 3, weight=6.1)

# Get attribute matrix using 'weight'
attribute_matrix = get_attribute_matrix(G, attribute='weight')
print(attribute_matrix)

# Get the adjacency matrix
adjacency_matrix = get_attribute_matrix(G)
print(adjacency_matrix)
