import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
# Replace with actual edges in the graph
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 7), (7, 5), (1, 5)]
G.add_edges_from(edges)

# Find weakly connected components in the graph
components = list(nx.weakly_connected_components(G))

# Compute Fiedler vector for each component
fiedler_vectors = []
for component in components:
    subgraph = G.subgraph(component)
    adjacency_matrix = nx.to_numpy_array(subgraph)
    eigenvalues, eigenvectors = np.linalg.eigh(adjacency_matrix)
    fiedler_vector = eigenvectors[:, 1]
    fiedler_vectors.append(fiedler_vector)

# Organize nodes by Fiedler vector elements
ordered_nodes = []
for vector in fiedler_vectors:
    indices = np.argsort(vector)
    ordered_component = [list(components[fiedler_vectors.index(vector)])[i] for i in indices]
    ordered_nodes.extend(ordered_component)

ordered_nodes
