import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Generate some nodes and edges for G
# ...

# Calculate the modularity of the graph
modularity = nx.modularity(G)

# Use the greedy algorithm to find communities
communities = nx.greedy_modularity_communities(G)

# Print the communities
for community in communities:
    print(community)
