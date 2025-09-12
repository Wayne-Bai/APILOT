import networkx as nx

# create a graph G
G = nx.Graph()

# add nodes to G
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

# add edges to G
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)

# find communities in G using greedy modularity maximization
communities = nx.greedy_modularity_communities(G)

# print the communities
print(communities)