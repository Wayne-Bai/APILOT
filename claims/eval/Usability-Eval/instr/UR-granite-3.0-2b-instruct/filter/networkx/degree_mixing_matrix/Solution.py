import networkx as nx

# Assuming G is your graph and attr is the attribute you want to use for mixing
def get_mixing_matrix(G, attr):
    # Compute the adjacency matrix
    adj_matrix = nx.to_numpy_array(G)

    # Compute the row sums of the adjacency matrix
    row_sums = np.sum(adj_matrix, axis=1)

    # Compute the column sums of the adjacency matrix
    col_sums = np.sum(adj_matrix, axis=0)

    # Compute the mixing matrix
    mixing_matrix = np.outer(row_sums, col_sums) / np.sum(adj_matrix)

    # If you want to use the attribute for mixing, you can modify the mixing matrix like this:
    # mixing_matrix *= attr

    return mixing_matrix
