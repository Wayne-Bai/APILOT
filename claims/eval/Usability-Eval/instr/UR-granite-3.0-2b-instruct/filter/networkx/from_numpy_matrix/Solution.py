import networkx as nx

# Assuming adj_matrix is your numpy matrix
adj_matrix = np.array([[0, 1, 0, 1],
                       [1, 0, 1, 0],
                       [0, 1, 0, 1],
                       [1, 0, 1, 0]])

# Create a graph from the adjacency matrix
G = nx.from_numpy_array(adj_matrix)

# Print the graph
print(G.edges())
