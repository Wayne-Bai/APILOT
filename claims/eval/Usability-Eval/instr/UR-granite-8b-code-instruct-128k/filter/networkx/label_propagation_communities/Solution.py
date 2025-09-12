import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Generate community sets using label propagation
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print the community sets
print(communities)
