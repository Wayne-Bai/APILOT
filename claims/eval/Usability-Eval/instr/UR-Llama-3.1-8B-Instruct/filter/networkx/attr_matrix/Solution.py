import networkx as nx
import numpy as np

def get_attribute_matrix(G, attribute=None):
    """
    Returns the attribute matrix using attributes from G as a numpy array.
    
    If only G is passed in, then the adjacency matrix is constructed.
    
    Parameters:
    G (graph): The input graph
    attribute (string, optional): The attribute to be used for the matrix construction. Defaults to None.
    
    Returns:
    np.ndarray: The attribute matrix as a numpy array
    """
    
    if attribute is not None:
        # Get the nodes that have the specified attribute
        nodes = [node for node in G.nodes if attribute in G.nodes[node]]
        
        # Get the attribute values from these nodes
        attr_values = [G.nodes[node][attribute] for node in nodes]
        
        # Create a matrix with the attribute values
        attr_matrix = np.array([[G.nodes[node][attribute] for node in G.nodes] for node in G.nodes])
        attr_matrix[nodes, :] = attr_values
        attr_matrix[:,nodes] = attr_values
        
        return attr_matrix
    
    else:
        # Get the adjacency matrix of the graph
        adj_matrix = nx.to_numpy_array(G)
        
        return adj_matrix

# Example usage:
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'C')

adj_matrix = get_attribute_matrix(G)
print(adj_matrix)

G.nodes['A']['color'] = 'Red'
G.nodes['B']['color'] = 'Blue'
G.nodes['C']['color'] = 'Green'

attr_matrix = get_attribute_matrix(G, attribute='color')
print(attr_matrix)
