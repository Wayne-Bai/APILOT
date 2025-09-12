import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
# Replace the following lines with your graph's data
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Compute the Google Matrix
n = len(G.nodes())
A = nx.to_numpy_array(G)
degrees = A.sum(axis=1)
D_inv = np.zeros((n,n))
np.fill_diagonal(D_inv, 1/degrees)

# Calculate the Google Matrix
google_matrix = np.dot(D_inv, A)
print("Google Matrix:")
print(google_matrix)
