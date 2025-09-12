import networkx as nx

# create a graph G
G = nx.Graph()

# add nodes and edges to G
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# find communities in G using greedy modularity maximization
communities = nx.greedy_modularity_communities(G)

# print the communities
print(communities)