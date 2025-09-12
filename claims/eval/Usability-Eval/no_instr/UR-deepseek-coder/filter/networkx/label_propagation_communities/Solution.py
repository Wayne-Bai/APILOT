import networkx as nx

# Create a sample graph
G = nx.karate_club_graph()

# Apply label propagation to find communities
communities = nx.algorithms.community.label_propagation_communities(G)

# Convert the communities to a list of sets
community_sets = list(communities)

# Print the community sets
for i, community in enumerate(community_sets):
    print(f"Community {i+1}: {community}")
