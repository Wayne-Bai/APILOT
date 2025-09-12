import networkx as nx
import scipy.sparse as sp

def graph_from_sparse_matrix(sparse_matrix):
    # Convert the sparse matrix to a NetworkX graph
    graph = nx.from_scipy_sparse_matrix(sparse_matrix)
    return graph

# Example usage
if __name__ == "__main__":
    # Create a sparse adjacency matrix
    sparse_matrix = sp.csr_matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    
    # Generate graph from the sparse matrix
    G = graph_from_sparse_matrix(sparse_matrix)
    
    # Print nodes and edges of the created graph
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())
