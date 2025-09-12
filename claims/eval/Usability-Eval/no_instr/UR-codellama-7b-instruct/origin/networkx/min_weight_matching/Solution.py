
import networkx as nx

# create a random graph
G = nx.gnp_random_graph(10, 0.5)

# compute the minimum weighted matching using the Edmonds-Karp algorithm
matching = nx.minimum_weighted_matching(G)

# print the resulting matching
print(matching)
