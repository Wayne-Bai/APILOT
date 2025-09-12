import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

def adjacency_matrix(graph):

    # getting the nodes in list
    nodes = list(graph.nodes())

    # getting the adjacency matrix (weights will be ignored)
    adj_matrix = nx.to_numpy_array(graph)

    # converting the adjacency matrix to a sparse matrix
    adj_matrix_sparse = csr_matrix(adj_matrix)

    # converting the sparse matrix to a recarray
    recarray = np.rec.fromarrays([adj_matrix_sparse.data, adj_matrix_sparse.indices, adj_matrix_sparse.indptr], names=['data', 'indices', 'indptr'])

    return recarray

# creating a simple graph
G = nx.Graph()

# Adding nodes to the graph
for node in range(5):
    G.add_node(node)

# Adding edges
edges = [(0,1),(1,2),(2,3),(3,4),(4,0)]
G.add_edges_from(edges)

# printing the adjacency matrix
print(adjacency_matrix(G))
