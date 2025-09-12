import networkx as nx
from scipy import sparse

# assuming we have a sparse adjacency list
data = [(0,1), (0,2), (1,2), (2,3), (2,4), (3,4)]
row = [e[0] for e in data]
col = [e[1] for e in data]
data = [1]*len(data)

# convert it to a sparse matrix
mat = sparse.coo_matrix((data, (row, col))).tocsr()

# convert the sparse matrix to a networkx graph
G = nx.from_scipy_sparse_matrix(mat)

# you can then use networkx functions to analyze G
print(G.number_of_nodes())
print(G.number_of_edges())
