import networkx as nx
from scipy.sparse import coo_matrix

# Assuming G is your graph
def graph_to_scipy_sparse_matrix(G):
    edges = [(u, v) for u, v in G.edges()]
    row, col = [], []
    for u, v in edges:
        row.append(u)
        col.append(v)
    data = [1] * len(edges) # Assuming edges are undirected and both edges are positive

    coo_matrix_data = coo_matrix((data, (row, col)))
    return coo_matrix_data.tocsr() # Convert to compressed sparse row format

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Convert the graph to a SciPy sparse matrix
adj_matrix = graph_to_scipy_sparse_matrix(G)
print(adj_matrix)
