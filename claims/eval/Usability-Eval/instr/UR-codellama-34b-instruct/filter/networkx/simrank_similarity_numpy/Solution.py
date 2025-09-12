import networkx as nx
import numpy as np

# Create a graph G with nodes and edges
G = nx.Graph()
G.add_nodes_from(["A", "B", "C"])
G.add_edges_from([("A", "B"), ("B", "C"), ("A", "C")])

# Calculate the SimRank matrix using NumPy
S = np.zeros((len(G), len(G)))
for i in range(len(G)):
    for j in range(i, len(G)):
        if G[i][j] == 1:
            S[i, j] = 1 / (len(G) - 1)
            S[j, i] = 1 / (len(G) - 1)
        else:
            S[i, j] = 0
            S[j, i] = 0

# Print the SimRank matrix
print(S)
