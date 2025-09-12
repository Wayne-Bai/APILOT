import numpy as np
import networkx as nx

G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E"])

G.add_weighted_edges_from([
    ("A", "B", 1),
    ("A", "C", 1),
    ("B", "D", 1),
    ("B", "E", 1),
    ("C", "D", 1),
    ("C", "E", 1)
])

n = G.number_of_nodes()
m = G.number_of_edges()
A = nx.adjacency_matrix(G, nodelist=sorted(G.nodes()))

alpha = 0.85
p = (1-alpha)/n

x = np.ones((n, 1)) / n
i = 0
while i < 100:
    x = alpha * (A @ x) + (1 - alpha) * p
    i += 1

sim_rank = (len(G)**2 - np.sum(A)**2 - (np.sum(A, axis=0) @ np.sum(A, axis=1)) )/ (n*(n-1)-np.sum(A)**2 )
print("SimRank of nodes in G: ", sim_rank[0])
