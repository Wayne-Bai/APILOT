
import networkx as nx

def spectral_ordering(G):
    """
    Compute the spectral ordering of a graph.

    The spectral ordering of a graph is an ordering of its nodes where nodes in the same weakly connected component appear contiguous and ordered by their corresponding elements in the Fiedler vector of the component.

    Parameters
    ----------
    G : NetworkX graph
        The input graph.

    Returns
    -------
    list
        A list of nodes in the spectral ordering.
    """
    # Compute the eigenvector of the graph Laplacian
    eigenvector = nx.laplacian_spectrum(G, weight='weight')[1]
    # Sort the nodes by their corresponding elements in the Fiedler vector
    return sorted(G.nodes(), key=lambda x: eigenvector[x])
