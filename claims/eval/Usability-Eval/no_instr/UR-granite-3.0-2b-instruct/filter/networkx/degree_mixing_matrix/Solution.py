import networkx as nx

def generate_mixing_matrix(G):
    """
    This function generates a mixing matrix for the given graph G.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    numpy.ndarray: A mixing matrix for the given graph.
    """
    # Get the degree of each node in the graph
    degrees = [d for _, d in G.degree()]

    # Calculate the total degree of the graph
    total_degree = sum(degrees)

    # Calculate the mixing matrix
    mixing_matrix = np.zeros((len(G), len(G)))
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j:
                mixing_matrix[i][j] = degrees[i] / total_degree
            else:
                mixing_matrix[i][j] = degrees[i] / (2 * total_degree)

    return mixing_matrix
