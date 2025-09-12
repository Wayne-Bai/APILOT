import networkx as nx

# Create an example graph
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)])

# Finding communities using greedy modularity maximization
communities = nx.community.greedy_modularity_communities(G)

# Printing communities
for idx, community in enumerate(communities):
    print(f"Community {idx}: {list(community)}")
