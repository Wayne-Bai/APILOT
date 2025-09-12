import networkx as nx
import numpy as np

# Define a random graph with 10 nodes
G = nx.fast_gnp_random_graph(10, 0.5)

# Print the adjacency matrix of the graph
print("Adjacency Matrix:")
print(nx.adjacency_matrix(G).toarray())

# Compute the PageRank of the nodes in the graph
pr = nx.pagerank(G, alpha=0.85, weight='weight')

# Print the PageRank of the nodes
print("\nPageRank of the nodes:")
print(pr)
