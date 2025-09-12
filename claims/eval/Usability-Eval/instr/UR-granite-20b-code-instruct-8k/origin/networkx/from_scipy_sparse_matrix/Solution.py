
import networkx as nx
def from_scipy_sparse_matrix(sparse_matrix):
    graph = nx.Graph(sparse_matrix)
    return graph
