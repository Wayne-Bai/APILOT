import networkx as nx
import scipy.sparse as sp

def graph_from_sparse_matrix(sparse_matrix):
    # Convert the sparse matrix to a COO format
    coo_matrix = sparse_matrix.tocoo()
    
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges to the graph from the COO matrix
    for i, j, value in zip(coo_matrix.row, coo_matrix.col, coo_matrix.data):
        G.add_edge(i, j, weight=value)
    
    return G

# Example usage:
# Assuming you have a scipy sparse matrix 'adj_matrix'
# G = graph_from_sparse_matrix(adj_matrix)
