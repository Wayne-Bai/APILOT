import networkx as nx
from scipy.sparse import csr_matrix

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Convert the graph to an adjacency matrix
adj_matrix = nx.adjacency_matrix(G).todense()

# Convert the dense matrix to a SciPy sparse matrix
sparse_matrix = csr_matrix(adj_matrix)

sparse_matrix
