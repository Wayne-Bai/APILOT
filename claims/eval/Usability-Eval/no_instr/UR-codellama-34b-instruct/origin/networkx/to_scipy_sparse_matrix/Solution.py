import numpy as np
import scipy.sparse as sp
from networkx import Graph

# Create an empty graph
G = Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Get the adjacency matrix as a SciPy sparse matrix
A = sp.lil_matrix(nx.adjacency_matrix(G))
