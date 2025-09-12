
import networkx as nx

# Load the graph from a file
G = nx.read_edgelist('your_file.txt', nodetype=int)

# Compute the HITS authority matrix
authority_matrix = nx.hits(G, max_iter=100, tol=1e-4)

# Print the authority matrix
print(authority_matrix)
