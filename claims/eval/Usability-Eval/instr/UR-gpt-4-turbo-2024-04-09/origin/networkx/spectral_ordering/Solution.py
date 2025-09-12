import networkx as nx
import numpy as np
from scipy.sparse.linalg import eigsh
from networkx import connected_components

def spectral_ordering(graph):
    if nx.is_directed(graph):
        # Use weakly connected components for directed graphs
        components = nx.weakly_connected_components(graph)
    else:
        # Use connected components for undirected graphs
        components = connected_components(graph)

    order = []
    for component in components:
        subgraph = graph.subgraph(component)
        laplacian = nx.laplacian_matrix(subgraph).astype(float)
        # Calculate the eigenvalues and eigenvectors
        eigenvals, eigenvects = eigsh(laplacian, k=2, which='SM')
        # Fiedler vector is the second smallest, i.e., eigenvects[:, 1]
        fiedler_vector = eigenvects[:, 1]
        # Sorting nodes by Fiedler vector
        sorted_nodes = sorted(component, key=lambda n: fiedler_vector[list(subgraph.nodes).index(n)])
        order.extend(sorted_nodes)
    
    return order
