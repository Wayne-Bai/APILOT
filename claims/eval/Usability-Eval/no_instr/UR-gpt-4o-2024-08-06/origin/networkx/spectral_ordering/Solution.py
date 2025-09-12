import networkx as nx
import numpy as np
from scipy.sparse.linalg import eigs

def spectral_ordering(graph):
    # Make sure the graph is undirected
    if graph.is_directed():
        graph = graph.to_undirected()

    # Get weakly connected components
    components = list(nx.connected_components(graph))
    ordering = []

    # Iterate over each component
    for component in components:
        subgraph = graph.subgraph(component)
        
        # Compute the Laplacian matrix
        L = nx.laplacian_matrix(subgraph).astype(float)

        # Compute the second smallest eigenvector (Fiedler vector)
        # Use smallest=False to indicate largest eigenvalues by magnitude
        _, vectors = eigs(L, k=2, which='SM')
        fiedler_vector = vectors[:, 1].real
        
        # Create a node list and sort according to the Fiedler vector
        nodes_fiedler = list(subgraph.nodes(data=False))
        nodes_fiedler_sorted = sorted(nodes_fiedler, key=lambda i: fiedler_vector[nodes_fiedler.index(i)])

        # Add to the overall ordering
        ordering.extend(nodes_fiedler_sorted)

    return ordering

# Example usage:
G = nx.Graph()
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (5, 6), (6, 7)]
G.add_edges_from(edges)

order = spectral_ordering(G)
print("Spectral ordering of the graph:", order)
