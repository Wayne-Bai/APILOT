import networkx as nx
import numpy as np

def numpy_to_gexf(matrix):
    G = nx.from_numpy_matrix(matrix)
    return G

# creating a numpy matrix
A = np.matrix([
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
])

G = numpy_to_gexf(A)

# print nodes and edges
print("Nodes of the graph:")
print(G.nodes())
print("\nEdges of the graph:")
print(G.edges())

# write graph to a.gexf file
nx.write_gexf(G, "numpy_graph.gexf")
