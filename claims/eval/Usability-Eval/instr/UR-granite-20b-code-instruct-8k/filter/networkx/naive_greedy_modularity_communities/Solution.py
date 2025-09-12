import networkx as nx

# Define the graph G
G = nx.Graph()

# Add edges to the graph G
# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(3, 4)
# G.add_edge(4, 5)
# G.add_edge(5, 6)
# G.add_edge(6, 1)

# Find communities in G using greedy modularity maximization
communities = nx.greedy_modularity_communities(G)

# Print the communities
print(communities)
