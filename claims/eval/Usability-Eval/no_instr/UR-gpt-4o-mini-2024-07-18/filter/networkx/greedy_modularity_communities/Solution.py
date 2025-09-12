import networkx as nx

# Create a sample graph (replace this with your own graph)
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (5, 6)])

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Convert the communities from a set of nodes to a list of lists for better readability
communities_list = [list(community) for community in communities]

# Print the detected communities
print("Detected communities:", communities_list)
