
import networkx as nx

# create a random graph with 10 nodes and edge between each pair of nodes
G = nx.gnp_random_graph(n=10, p=0.5)

# print adjacency matrix of G
print(nx.adjacency_matrix(G))
