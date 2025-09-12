
import networkx as nx
import numpy as np

def get_fiedler_vector(graph):
    laplacian = nx.normalized_laplacian_matrix(graph).todense()
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    fiedler_vector = eigenvectors[:, 1]
    return fiedler_vector

def spectral_ordering(graph):
    weakly_connected_components = list(nx.weakly_connected_components(graph))
    spectral_order = []
    
    for component_nodes in weakly_connected_components:
        component_graph = graph.subgraph(component_nodes)
        fiedler_vector = get_fiedler_vector(component_graph)
        node_order = [node for _, node in sorted(zip(fiedler_vector, component_nodes))]
        spectral_order.extend(node_order)
    
    return spectral_order

# Example usage
G = nx.gnp_random_graph(10, 0.3)
ordering = spectral_ordering(G)
print(ordering)
