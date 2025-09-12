import networkx as nx
import numpy as np

# Creating a new graph
G = nx.Graph()

# Adding nodes to the graph
nodes = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodes)

# Adding edges to the graph
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
G.add_edges_from(edges)

# Converting the graph into adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Creating a numpy recarray from the adjacency matrix
adj_recarray = np.array(adj_matrix, dtype=[('var{}'.format(i), int) for i in range(len(nodes))])

print(adj_recarray)
