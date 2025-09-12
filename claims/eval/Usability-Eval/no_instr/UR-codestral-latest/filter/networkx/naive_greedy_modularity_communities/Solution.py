import networkx as nx

# Assuming you have a graph G
# If you don't have a graph, you can create a simple graph using
# G = nx.Graph()

# Find communities in G
communities = list(nx.community.greedy_modularity_communities(G))

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i}: {community}")
