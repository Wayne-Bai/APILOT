
import networkx as nx

# Generate a random graph using Barabasi–Albert preferential attachment
n = 10  # Number of nodes
m = 2  # Number of edges to attach from a new node to existing nodes

G = nx.barabasi_albert_graph(n, m)

# Print the adjacency matrix of the graph
print(nx.adj_matrix(G).todense())

