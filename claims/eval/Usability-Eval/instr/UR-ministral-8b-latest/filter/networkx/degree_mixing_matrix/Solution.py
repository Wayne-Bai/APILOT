import networkx as nx

def get_mixing_matrix(G):
    """
    Calculate the mixing matrix for a graph G.

    Parameters:
    G (networkx.Graph): The graph for which to calculate the mixing matrix.

    Returns:
    dict: The mixing matrix.
    """
    if not isinstance(G, nx.Graph):
        raise TypeError("Input must be a networkx Graph object.")

    n = G.number_of_nodes()
    mixing_matrix = {i: {j: 0 for j in range(n)} for i in range(n)}

    for u, v in G.edges():
        mixing_matrix[u][v] = 1
        mixing_matrix[v][u] = 1

    return mixing_matrix

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (0, 2), (1, 3)])

# Get the mixing matrix
mixing_matrix = get_mixing_matrix(G)
print(mixing_matrix)
