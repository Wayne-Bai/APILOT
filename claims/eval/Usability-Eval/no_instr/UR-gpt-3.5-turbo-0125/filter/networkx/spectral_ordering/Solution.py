import networkx as nx
import numpy as np

def spectral_ordering(G):
    weakly_connected_components = list(nx.weakly_connected_components(G))
    ordering = []

    for component in weakly_connected_components:
        subgraph = G.subgraph(component)
        L = nx.normalized_laplacian_matrix(subgraph).todense()
        eigenvalues, eigenvectors = np.linalg.eigh(L)
        fiedler_vector = eigenvectors[:, 1]  # Fiedler vector corresponds to the second smallest eigenvalue

        nodes_sorted_by_fiedler = [node for _, node in sorted(zip(fiedler_vector, component))]

        ordering.extend(nodes_sorted_by_fiedler)

    return ordering

# Example usage
G = nx.DiGraph([(1, 2), (2, 3), (2, 4), (5, 6), (6, 7)])
ordering = spectral_ordering(G)
print(ordering)
