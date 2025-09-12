import networkx as nx
import numpy as np

def spectral_ordering(G):
    # Compute the weakly connected components
    components = list(nx.weakly_connected_components(G))
    
    # Initialize the ordering list
    ordering = []
    
    for component in components:
        # Create a subgraph for the current component
        subgraph = G.subgraph(component)
        
        # Compute the Laplacian matrix of the subgraph
        L = nx.laplacian_matrix(subgraph).toarray()
        
        # Compute the Fiedler vector (second smallest eigenvector of the Laplacian)
        eigenvalues, eigenvectors = np.linalg.eigh(L)
        fiedler_vector = eigenvectors[:, 1]
        
        # Sort the nodes based on the Fiedler vector
        sorted_nodes = sorted(subgraph.nodes(), key=lambda node: fiedler_vector[list(subgraph.nodes()).index(node)])
        
        # Append the sorted nodes to the ordering list
        ordering.extend(sorted_nodes)
    
    return ordering

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (5, 6), (6, 7)])
ordering = spectral_ordering(G)
print("Spectral Ordering:", ordering)
