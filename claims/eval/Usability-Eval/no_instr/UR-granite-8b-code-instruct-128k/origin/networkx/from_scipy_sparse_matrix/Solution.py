import networkx as nx
import scipy.sparse as sp

def generate_graph_from_adjacency_list(adjacency_list):
    # Convert the adjacency list to a scipy sparse matrix
    adjacency_matrix = sp.csr_matrix(adjacency_list)

    # Generate the graph from the adjacency matrix
    graph = nx.from_scipy_sparse_matrix(adjacency_matrix)

    return graph
