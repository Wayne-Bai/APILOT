import networkx as nx
import numpy as np

def spectral_ordering(G):
    # Write G into an arranged structure
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G)

    # Compute the Fiedler vector using the symmetric normalized Laplacian matrix 
    L = nx.linalg.normalized_laplace_matrix(G)
    u, _, Vh = np.linalg.svd(L)
    fiedler_vector = Vh[-1:, :]  # Get last row of Vh (corresponds to last eigenvalue

    # Initialize the ordering vector
    ordering = np.ones(n)

    # Iterate over weakly connected components
    for component in nx.weakly_connected_components(G):
        component_nodes = list(component)
        component_A = A[component_nodes, :][:, component_nodes]
        component_fiedler_vector = fiedler_vector[:, component_nodes]

        # Sort nodes in the component based on the Fiedler vector
        sorted_component_nodes = np.argsort(component_fiedler_vector)[::-1]
        for i, node in enumerate(sorted_component_nodes):
            ordering[component_nodes.index(node)] = i + 1

    return ordering

# Example usage:
G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4), (5, 6), (5, 7)])
print(spectral_ordering(G))
