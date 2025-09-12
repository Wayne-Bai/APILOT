import networkx as nx

# Assume G is your graph
# G = ...

# Use greedy_modularity_communities function to find communities
communities = list(nx.community.greedy_modularity_communities(G))

print("Number of communities found:", len(communities))
for i, community in enumerate(communities):
    print(f"Community {i}: {community}")
