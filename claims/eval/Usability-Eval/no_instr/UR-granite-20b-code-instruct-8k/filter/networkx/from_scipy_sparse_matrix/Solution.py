
import networkx as nx
def create_graph(matrix):
    graph = nx.from_scipy_sparse_matrix(matrix)
    return graph
