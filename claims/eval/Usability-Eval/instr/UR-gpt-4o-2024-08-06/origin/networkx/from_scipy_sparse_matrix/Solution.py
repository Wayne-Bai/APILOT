import networkx as nx
from scipy.sparse import csr_matrix

def sparse_matrix_to_graph(sparse_matrix):
    """
    Converts a SciPy sparse adjacency matrix to a NetworkX graph.

    Parameters:
    sparse_matrix (scipy.sparse.csr_matrix): The SciPy sparse matrix representing adjacency.

    Returns:
    G (networkx.Graph): The NetworkX graph corresponding to the sparse matrix.
    """
    # Convert the sparse matrix to a COO format for easy iteration
    coo_matrix = sparse_matrix.tocoo()

    # Create a new graph
    G = nx.Graph()

    # Add edges to the graph
    for i, j, v in zip(coo_matrix.row, coo_matrix.col, coo_matrix.data):
        G.add_edge(i, j, weight=v)

    return G

# Example usage:
# Define a sparse matrix
sparse_adj_matrix = csr_matrix([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

# Convert the sparse matrix to a NetworkX graph
graph = sparse_matrix_to_graph(sparse_adj_matrix)

# Print the edges with weights to verify
for (u, v, wt) in graph.edges(data='weight'):
    print(f"Edge from {u} to {v} with weight {wt}")
