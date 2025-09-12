import networkx as nx
import numpy as np
from scipy.sparse.linalg import eigs
from networkx.utils import not_implemented_for

@not_implemented_for('directed')
def spectral_ordering(G):
    # Sorting function for the components based on the Fiedler vector
    def component_ordering(component):
        # Create a subgraph for the component
        H = G.subgraph(component)
        
        # Get the Laplacian matrix
        L = nx.laplacian_matrix(H).astype(float)
        
        # Calculate Fiedler vector using eigen decomposition
        # eigs returns the eigenvalues and eigenvectors
        _, vectors = eigs(L, k=2, which='SR')
        fiedler_vector = vectors[:, 1]
        
        # Map nodes to their Fiedler vector values and sort
        node_fiedler = {node: fiedler_vector[i].real for i, node in enumerate(H.nodes())}
        return sorted(H.nodes(), key=lambda x: node_fiedler[x])
    
    # Find weakly connected components
    components = list(nx.connected_components(G))
    
    # Order nodes in each component
    ordered_nodes = []
    for component in components:
        ordered_nodes.extend(component_ordering(component))
    
    return ordered_nodes

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (5, 6)])
    
    # Get the spectral ordering
    ordering = spectral_ordering(G)
    print("Spectral Ordering of the Graph:", ordering)
