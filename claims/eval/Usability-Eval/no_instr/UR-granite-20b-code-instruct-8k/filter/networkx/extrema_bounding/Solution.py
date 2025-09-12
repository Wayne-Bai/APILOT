
import networkx as nx
# create an undirected graph
G = nx.Graph()
# add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
# compute the extreme distance metric
extreme_distance = nx.extremes.extreme_distance(G)
# print the result
print(extreme_distance)
