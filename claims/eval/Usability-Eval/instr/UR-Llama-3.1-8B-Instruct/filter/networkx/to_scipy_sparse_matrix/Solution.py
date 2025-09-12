import networkx as nx
from scipy import sparse

# Create an example graph
G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Convert the graph to an adjacency matrix using the 'csr' format
adj_matrix_csr = sparse.csr_matrix(nx.to_numpy_array(G))

# Convert the graph to an adjacency matrix using the 'csc' format
adj_matrix_csc = sparse.csc_matrix(nx.to_numpy_array(G))

# Convert the graph to an adjacency matrix using the 'bsr' format
adj_matrix_bsr = sparse.bsr_matrix(nx.to_numpy_array(G))

# Convert the graph to an adjacency matrix using the 'dia' format
adj_matrix_dia = sparse.dia_matrix(nx.to_numpy_array(G))

print(adj_matrix_csr.toarray())  # Convert back to array for printing
print(adj_matrix_csc.toarray())  # Convert back to array for printing
print(adj_matrix_bsr.toarray())  # Convert back to array for printing
print(adj_matrix_dia.toarray())  # Convert back to array for printing
