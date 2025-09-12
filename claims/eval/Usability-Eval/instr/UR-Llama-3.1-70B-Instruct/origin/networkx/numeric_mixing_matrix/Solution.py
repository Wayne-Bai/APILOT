import networkx as nx
import numpy as np
import pandas as pd

# Function to calculate the mixing matrix for a given attribute
def mixing_matrix(G, attribute):
    # Get all nodes from the graph
    nodes = list(G.nodes())

    # Initialize an empty matrix filled with zeros
    mixing_matrix = np.zeros((len(nodes), len(nodes)))

    # Iterate over all edges in the graph
    for u, v in G.edges():
        # Get the attribute values for both nodes
        u_attribute = G.nodes[u].get(attribute)
        v_attribute = G.nodes[v].get(attribute)

        # If both nodes have the attribute, increment the corresponding matrix entry
        if u_attribute is not None and v_attribute is not None:
            mixing_matrix[nodes.index(u), nodes.index(v)] += 1
            mixing_matrix[nodes.index(v), nodes.index(u)] += 1  # If the graph is undirected

    # Normalize the matrix by the degree of each node
    degrees = dict(G.degree())
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if degrees[nodes[i]] > 0:
                mixing_matrix[i, j] /= degrees[nodes[i]]

    return mixing_matrix


# Example usage
# Create an empty graph
G = nx.Graph()

# Add nodes with an attribute
G.add_node('A', type='A')
G.add_node('B', type='A')
G.add_node('C', type='B')
G.add_node('D', type='B')

# Add edges between nodes
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Calculate the mixing matrix for the 'type' attribute
matrix = mixing_matrix(G, 'type')

# Print the resulting matrix
print(matrix)
