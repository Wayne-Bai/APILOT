import networkx as nx
import numpy as np

def spectral_ordering(G):
    # Get weakly connected components
    components = list(nx.weakly_connected_components(G))
    ordered_nodes = []
    
    for component in components:
        subgraph = G.subgraph(component)
        
        # Calculate the Laplacian matrix
        laplacian = nx.laplacian_matrix(subgraph).toarray()
        
        # Calculate the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(laplacian)
        
        # Get the index of the second smallest eigenvalue (the Fiedler vector)
        idx = np.argsort(eigenvalues)[1]
        fiedler_vector = eigenvectors[:, idx]
        
        # Sort nodes based on the Fiedler vector
        sorted_nodes = sorted(component, key=lambda x: fiedler_vector[component.index(x)])
        ordered_nodes.extend(sorted_nodes)
    
    return ordered_nodes

# Example usage
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (3, 4), (4, 5), (5, 3)])
ordering = spectral_ordering(G)
print(ordering)
