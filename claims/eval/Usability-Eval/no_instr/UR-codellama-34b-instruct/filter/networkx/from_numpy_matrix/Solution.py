import networkx as nx

# Define the NumPy matrix
matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Create a graph from the NumPy matrix
G = nx.from_numpy_matrix(matrix)

# Print the adjacency list of the graph
print(list(nx.adjacency_list(G)))
