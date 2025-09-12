import networkx as nx

def spectral_ordering(graph):
    adjacency_matrix = nx.adjacency_matrix(graph)
    eigenvalues, eigenvectors = nx.linalg.eigs(adjacency_matrix, k=1, which='SM')
    fiedler_vector = eigenvectors.flatten()
    weakly_connected_components = nx.weakly_connected_components(graph)
    ordering = []
    for component in weakly_connected_components:
        component_nodes = list(component)
        component_fiedler_values = [fiedler_vector[node] for node in component_nodes]
        sorted_nodes = [node for _, node in sorted(zip(component_fiedler_values, component_nodes))]
        ordering.extend(sorted_nodes)
    
    return ordering
