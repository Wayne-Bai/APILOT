import networkx as nx
import numpy as np

def spectral_ordering(graph):
    # Ensure the graph is directed
    if not nx.is_directed(graph):
        raise ValueError("The input graph must be directed.")
    
    # Get the weakly connected components
    components = list(nx.weakly_connected_components(graph))
    
    # Prepare the final ordering
    final_ordering = []
    
    for component in components:
        subgraph = graph.subgraph(component)
        
        # Compute the Laplacian matrix for the subgraph
        laplacian = nx.laplacian_matrix(subgraph).A
        
        # Compute the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(laplacian)
        
        # Get the Fiedler vector (the eigenvector corresponding to the second smallest eigenvalue)
        fiedler_vector = eigenvectors[:, np.argsort(eigenvalues)[1]]

        # Order nodes based on the Fiedler vector
        sorted_nodes = [node for _, node in sorted(zip(fiedler_vector, component))]
        
        # Append to the final ordering
        final_ordering.extend(sorted_nodes)
    
    return final_ordering

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])
# ordered_nodes = spectral_ordering(G)
# print(ordered_nodes)
