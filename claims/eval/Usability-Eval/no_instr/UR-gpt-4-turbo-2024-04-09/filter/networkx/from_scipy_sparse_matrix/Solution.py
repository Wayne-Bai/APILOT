import networkx as nx
import scipy.sparse

def create_graph_from_scipy_sparse_matrix(matrix):
    # Create a graph from a Scipy sparse matrix adjacency list
    G = nx.from_scipy_sparse_matrix(matrix)
    return G

# Example usage:
# Assuming you have a scipy sparse matrix `sparse_matrix` ready for this example
# sparse_matrix = scipy.sparse.csr_matrix([...])

# Uncomment the line below to test with your matrix
# G = create_graph_from_scipy_sparse_matrix(sparse_matrix)
# print(G.edges())
