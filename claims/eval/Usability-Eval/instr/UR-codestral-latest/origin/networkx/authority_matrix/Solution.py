import networkx as nx

# create a test graph
G = nx.DiGraph()

# add some edges
edges = [(1,2), (2,3), (3,4), (4,1)]
G.add_edges_from(edges)

# compute HITS and store the scores for each node in two variables -- hubs and authorities
hubs, authorities = nx.hits(G)

# print hubs
print("Hubs: ", hubs)

# print authorities
print("Authorities: ", authorities)
