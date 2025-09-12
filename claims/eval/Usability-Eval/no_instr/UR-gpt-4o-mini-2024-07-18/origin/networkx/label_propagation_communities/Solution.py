import networkx as nx

# Create a sample graph
G = nx.Graph()
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4)]
G.add_edges_from(edges)

# Perform label propagation
communities = nx.algorithms.community.label_propagation_communities(G)

# Convert to a list of sets
community_sets = [set(community) for community in communities]

# Print the communities
print("Detected Communities:")
for idx, community in enumerate(community_sets):
    print(f"Community {idx + 1}: {community}")
