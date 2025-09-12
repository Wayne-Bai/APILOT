import networkx as nx

# Create a graph
G = nx.karate_club_graph()

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print the communities
for i, community in enumerate(communities, 1):
    print(f"Community {i}: {sorted(community)}")
