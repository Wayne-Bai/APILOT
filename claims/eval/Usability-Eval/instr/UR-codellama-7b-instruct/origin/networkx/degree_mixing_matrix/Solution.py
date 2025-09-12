
import networkx as nx

# Create a random graph
G = nx.gnm_random_graph(10, 3, directed=False)

# Get the degree distribution of the graph
degree_dist = G.degree()

# Normalize the degree distribution to obtain a mixing matrix
mixing_matrix = np.zeros((len(G), len(G)))
for i in range(len(G)):
    for j in range(i+1, len(G)):
        mixing_matrix[i][j] = G[i][j] / degree_dist[i]

# Print the mixing matrix
print(mixing_matrix)
