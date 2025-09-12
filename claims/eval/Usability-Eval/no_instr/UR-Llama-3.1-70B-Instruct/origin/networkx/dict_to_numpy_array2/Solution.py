import networkx as nx
import numpy as np

def dict_of_dict_to_numpy_array(graph_dict, mapping=None):
    """
    Converts a dictionary of dictionaries to a 2d numpy array.
    
    Args:
    graph_dict (dict): A dictionary of dictionaries.
    mapping (dict, optional): Optional mapping for node to index. Defaults to None.
    
    Returns:
    numpy array: A 2d numpy array representation of the graph.
    """

    # Check if graph_dict is a dictionary of dictionaries
    if not isinstance(graph_dict, dict) or not all(isinstance(sub_dict, dict) for sub_dict in graph_dict.values()):
        raise ValueError("Input must be a dictionary of dictionaries")

    # Get all unique nodes from the graph dictionary
    nodes = set()
    for node, neighbors in graph_dict.items():
        nodes.add(node)
        nodes.update(neighbors)

    # If no mapping is provided, create a default one
    if mapping is None:
        mapping = {node: i for i, node in enumerate(nodes)}
    
    # Get the number of nodes
    num_nodes = len(nodes)
    
    # Initialize an adjacency matrix
    adj_matrix = np.zeros((num_nodes, num_nodes))
    
    # Populate the adjacency matrix
    for node, neighbors in graph_dict.items():
        for neighbor, weight in neighbors.items():
            adj_matrix[mapping[node], mapping[neighbor]] = weight
    
    return adj_matrix

# Example usage
graph_dict = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 1},
    'F': {'C': 4}
}

adj_matrix = dict_of_dict_to_numpy_array(graph_dict)
print(adj_matrix)
