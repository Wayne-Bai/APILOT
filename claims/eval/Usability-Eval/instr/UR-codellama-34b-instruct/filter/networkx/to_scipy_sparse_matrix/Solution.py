
import numpy as np
import scipy.sparse as sp
from networkx import Graph

# create a graph with some nodes and edges
G = Graph()
G.add_nodes_from(["A", "B", "C", "D"])
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")])

# get the adjacency matrix as a sparse matrix
A = sp.csr_matrix(nx.adjacency_matrix(G))
