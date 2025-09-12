
import networkx as nx

# create a random graph with 10 nodes and 20 edges
G = nx.random_graphs.RandomGraph(10, 20)

# compute mixing matrix for each node
mixing_matrix = nx.mixing_matrix(G)

print("Mixing Matrix:")
print(mixing_matrix)
