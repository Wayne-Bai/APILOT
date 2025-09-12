import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print the communities
for community in communities:
    print(community)
