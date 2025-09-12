import networkx as nx
from scipy.optimize import linear_sum_assignment

# Define the graph structure
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Perform a shortest-path graph search using Floyd-Warshall algorithm
distances = nx.floyd_warshall_shortest_paths(G)
