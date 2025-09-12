
import numpy as np
import networkx as nx

# Load the sparse matrix
sparse_matrix = np.loadtxt('your_file.mtx')

# Create a directed graph from the sparse matrix
G = nx.from_scipy_sparse_matrix(sparse_matrix, create_using=nx.DiGraph())
