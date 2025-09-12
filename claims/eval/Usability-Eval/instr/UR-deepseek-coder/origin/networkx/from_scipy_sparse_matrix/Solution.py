import networkx as nx
import scipy.sparse as sp

def graph_from_sparse_matrix(sparse_matrix):
    # Convert the sparse matrix to a COO format
    coo_matrix = sparse_matrix.tocoo()
    
    # Create an empty graph
    G = nx.Graph()
    
    # Add edges to the graph based on the COO matrix
    for i, j, v in zip(coo_matrix.row, coo_matrix.col, coo_matrix.data):
        if v != 0:  # Only add non-zero edges
            G.add_edge(i, j, weight=v)
    
    return G

# Example usage:
# Assuming you have a scipy sparse matrix 'adj_matrix'
# G = graph_from_sparse_matrix(adj_matrix)
