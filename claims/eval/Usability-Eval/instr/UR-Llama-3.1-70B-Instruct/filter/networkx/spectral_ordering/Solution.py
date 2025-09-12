import networkx as nx
import numpy as np

def spectral_ordering(G):
    """
    Compute the spectral ordering of a graph.

    The spectral ordering of a graph is an ordering of its nodes where nodes in the
    same weakly connected components appear contiguous and ordered by their
    corresponding elements in the Fiedler vector of the component.

    Parameters
    ----------
    G : NetworkX Graph
        The graph to compute the spectral ordering for.

    Returns
    -------
    ordering : list
        The spectral ordering of the graph.
    """
    if not isinstance(G, nx.Graph):
        raise nx.NetworkXError("Input graph must be a simple graph")

    # Get the connected components
    components = list(nx.connected_components(G))

    # Initialize the ordering
    ordering = []

    # Loop over the components
    for component in components:
        # Create a subgraph for the component
        subgraph = G.subgraph(component)

        # Get the adjacency matrix of the subgraph
        A = nx.to_numpy_array(subgraph)

        # Compute the Laplacian of the subgraph
        L = np.diag(np.sum(A, axis=1)) - A

        # Compute the eigenvectors and eigenvalues of the Laplacian
        eigenvalues, eigenvectors = np.linalg.eigh(L)

        # Get the Fiedler vector (the second smallest eigenvector)
        fiedler_vector = eigenvectors[:, 1]

        # Order the nodes in the component by the Fiedler vector
        ordered_nodes = sorted(list(component), key=lambda node: fiedler_vector[list(subgraph.nodes).index(node)])

        # Add the ordered nodes to the ordering
        ordering.extend(ordered_nodes)

    return ordering

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)])

# Compute the spectral ordering
ordering = spectral_ordering(G)

# Print the ordering
print(ordering)
