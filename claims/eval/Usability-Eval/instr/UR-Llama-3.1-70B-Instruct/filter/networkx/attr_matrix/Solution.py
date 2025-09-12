import networkx as nx
import numpy as np

def get_attribute_matrix(G, attributes=None):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    
    Parameters:
    G (networkx graph): The input graph.
    attributes (list, optional): A list of node attributes to include in the matrix. 
                                 Defaults to None, in which case the adjacency matrix is constructed.
    
    Returns:
    numpy array: The attribute matrix or adjacency matrix.
    """
    
    # Check if the graph is empty
    if not G:
        return np.array([])
    
    # Get the nodes of the graph
    nodes = list(G.nodes())
    
    # Get the number of nodes
    num_nodes = len(nodes)
    
    # If attributes are not specified, construct the adjacency matrix
    if attributes is None:
        # Use the adjacency_matrix function from networkx
        A = nx.to_numpy_array(G, nodelist=nodes)
        return A
    
    # Initialize an empty attribute matrix
    attribute_matrix = np.zeros((num_nodes, len(attributes)))
    
    # Iterate over nodes and attributes
    for i, node in enumerate(nodes):
        for j, attr in enumerate(attributes):
            # Check if the node has the attribute
            if attr in G.nodes[node]:
                attribute_matrix[i, j] = G.nodes[node][attr]
    
    return attribute_matrix

# Create an example graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3], weight=1.0)
G.add_edge(1, 2, capacity=15.0, weight=2)
G.add_edge(2, 3, capacity=20.0, weight=3)
G.add_edge(3, 1, capacity=10.0, weight=4)

# Get the attribute matrix for a specific set of attributes
attribute_matrix = get_attribute_matrix(G, attributes=['weight'])

# Get the adjacency matrix
adjacency_matrix = get_attribute_matrix(G)

print("Attribute Matrix:")
print(attribute_matrix)
print("\nAdjacency Matrix:")
print(adjacency_matrix)
