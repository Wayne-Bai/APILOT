import networkx as nx

# Create a graph object
G = nx.Graph()

# Add edges (assuming edges are added as a list of tuples)
# Connecting nodes 1 and 2, 1 and 3, 2 and 3, and so on
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
G.add_edges_from(edges)

# Use the greedy modularity maximization to find communities
communities = list(nx.community.greedy_modularity_communities(G))

# Print the resulting communities
for community in communities:
    print(community)
