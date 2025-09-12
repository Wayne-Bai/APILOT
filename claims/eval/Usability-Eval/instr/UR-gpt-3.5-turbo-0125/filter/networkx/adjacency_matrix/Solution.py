
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Get nodes in the graph
nodes = list(G.nodes())

# Create an empty adjacency matrix
adj_matrix = [[0]*len(nodes) for _ in range(len(nodes))]

# Fill the adjacency matrix using edges
for edge in G.edges():
    adj_matrix[nodes.index(edge[0])][nodes.index(edge[1])] = 1
    adj_matrix[nodes.index(edge[1])][nodes.index(edge[0])] = 1

print(adj_matrix)
