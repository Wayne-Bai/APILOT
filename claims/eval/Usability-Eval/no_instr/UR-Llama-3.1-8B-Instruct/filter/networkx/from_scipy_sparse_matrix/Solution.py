import networkx as nx
import scipy.sparse as sp

def matrix_to_graph(adj_matrix):
    """
    Create a graph from a scipy sparse adjacency matrix.
    
    Parameters:
    adj_matrix (scipy.sparse.csr_matrix or scipy.sparse.csc_matrix): The adjacency matrix of the graph.
    
    Returns:
    G (networkx.Graph or networkx.DiGraph): The graph represented by the adjacency matrix.
    """
    if not isinstance(adj_matrix, (sp.csr_matrix, sp.csc_matrix)):
        raise ValueError("Input must be a scipy sparse matrix")
    
    adj_array = adj_matrix.toarray()  # convert sparse matrix to dense array
    
    # create a directed graph
    G = nx.DiGraph()
    
    # add edges to the graph
    for i in range(adj_array.shape[0]):
        for j in range(adj_array.shape[1]):
            if adj_array[i, j]!= 0:
                G.add_edge(i, j)
    
    return G

# example usage:
adj_matrix = sp.coo_matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
G = matrix_to_graph(adj_matrix)
print(nx.info(G))
