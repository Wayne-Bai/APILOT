import networkx as nx

# Create a sample graph
G = nx.karate_club_graph()

# Use the greedy modularity communities function
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print communities
for community in communities:
    print(sorted(community))
