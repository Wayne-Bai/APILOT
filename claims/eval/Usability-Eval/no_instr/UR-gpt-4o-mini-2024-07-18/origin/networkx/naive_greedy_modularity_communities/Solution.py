import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 4)])

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i + 1}: {community}")
