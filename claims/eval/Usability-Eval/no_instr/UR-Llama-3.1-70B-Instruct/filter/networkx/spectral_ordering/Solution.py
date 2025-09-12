import networkx as nx
import numpy as np

def spectral_ordering(G):
    """
    Compute the spectral ordering of a graph.

    Parameters:
    G (NetworkX graph)
    An undirected graph.

    Returns:
    ordering (list)
    An list of nodes representing the spectral ordering of the graph.
    """
    # Get the weakly connected components
    components = [c for c in nx.weakly_connected_components(G)]
    
    # Initialize the ordering list
    ordering = []
    
    # For each component, compute the spectral ordering
    for component in components:
        # Get the subgraph of the current component
        component_graph = G.subgraph(component)
        
        # Compute the Laplacian matrix of the subgraph
        laplacian_matrix = nx.linalg.laplacianmatrix.laplacian_matrix(component_graph)
        
        # Compute the eigenvectors of the Laplacian matrix
        eigenvectors = np.linalg.eig(laplacian_matrix.A)[1]
        
        # Get the Fiedler vector (the eigenvector corresponding to the second smallest eigenvalue)
        fiedler_vector = eigenvectors[:, 1]
        
        # Get the nodes of the component ordered by their corresponding elements in the Fiedler vector
        ordered_nodes = sorted(list(component), key=lambda x: fiedler_vector[list(component).index(x)])
        
        # Add the ordered nodes of the current component to the overall ordering
        ordering.extend(ordered_nodes)
    
    return ordering

# Example usage:
G = nx.gnp_random_graph(20, 0.1)
print(spectral_ordering(G))
