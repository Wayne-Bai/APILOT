import networkx as nx
import numpy as np

def attribute_matrix(G, attribute=None):
    if attribute is None:
        # Return the adjacency matrix if no attribute is specified
        return nx.to_numpy_array(G)
    else:
        # Return the attribute matrix where each element is an attribute of the node
        attr_values = nx.get_node_attributes(G, attribute)
        n = len(G)
        matrix = np.zeros((n, n))
        for i, node_i in enumerate(G.nodes):
            for j, node_j in enumerate(G.nodes):
                if node_i in G[node_j]:  # Check if there is an edge
                    # Use attributes of the node for matrix values if the edge exists
                    matrix[i, j] = attr_values.get(node_i, 0)
        return matrix

# Example usage:
# Create a directed graph for demonstration
G = nx.DiGraph()
G.add_node(1, weight=2)
G.add_node(2, weight=3)
G.add_node(3, weight=5)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Get the adjacency matrix
adj_matrix = attribute_matrix(G)
print("Adjacency Matrix:")
print(adj_matrix)

# Get the attribute matrix based on node weights
weight_matrix = attribute_matrix(G, 'weight')
print("Weight Matrix:")
print(weight_matrix)
