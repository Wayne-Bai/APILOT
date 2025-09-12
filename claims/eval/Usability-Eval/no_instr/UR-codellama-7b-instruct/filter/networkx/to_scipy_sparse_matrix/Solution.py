
import networkx as nx
from scipy.sparse import lil_matrix

# create a sample graph
G = nx.Graph()
G.add_nodes_from([0, 1, 2])
G.add_edges_from([(0, 1), (1, 2)])

# convert the graph to an adjacency matrix using SciPy's lil_matrix
A = nx.to_scipy_sparse_matrix(G, format="lil")

print(A)
