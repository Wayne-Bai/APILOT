import networkx as nx
import numpy as np
import scipy.sparse.linalg

def spectral_ordering(graph):
    # Determine connected components
    if nx.is_directed(graph):
        components = list(nx.weakly_connected_components(graph))
    else:
        components = list(nx.connected_components(graph))
        
    # Container for the spectral ordering of nodes
    node_order = []

    # Process each component
    for component in components:
        subgraph = graph.subgraph(component)
        
        if len(component) > 1:
            # Compute the Laplacian matrix of the subgraph
            L = nx.laplacian_matrix(subgraph).astype(float)
            
            # Compute the eigenvalues and eigenvectors
            eigenvalues, eigenvectors = scipy.sparse.linalg.eigsh(L, k=2, which='SM')
            
            # The Fiedler vector is the eigenvector corresponding to the second smallest eigenvalue
            fiedler_vector = eigenvectors[:, 1]
            
            # Order nodes by the Fiedler vector
            nodes_sorted_by_fiedler = [node for _, node in sorted(zip(fiedler_vector, subgraph.nodes()))]
        else:
            # Only one node, trivial order
            nodes_sorted_by_fiedler = list(component)
        
        # Append this component's order to the overall node order
        node_order.extend(nodes_sorted_by_fiedler)

    return node_order

# Example usage:
G = nx.path_graph(10, create_using=nx.DiGraph())    # Directed graph example
print(spectral_ordering(G))
