import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs

def spectral_ordering(G):
    # Compute the Laplacian matrix
    L = csr_matrix(nx.laplacian_matrix(G).toarray())

    # Compute the Fiedler vector
    eigenvalues, eigenvectors = eigs(L, k=1, which='SM')
    fiedler_vector = eigenvectors.T[0]

    # Compute the spectral ordering
    spectral_ordering = []
    components = nx.weakly_connected_components(G)
    for component in components:
        component_indices = [i for i in range(len(G.nodes())) if i in component]
        spectral_ordering.extend(component_indices[sorted(range(len(component_indices)), key=lambda k: fiedler_vector[k])])

    return spectral_ordering
