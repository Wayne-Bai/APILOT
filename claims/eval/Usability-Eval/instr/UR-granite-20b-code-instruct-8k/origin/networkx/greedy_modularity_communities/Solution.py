import networkx as nx

# Generate your graph G
G = nx.Graph()

# Add edges to the graph G
# G.add_edge(node1, node2)

# Find communities in G using greedy modularity maximization
communities = nx.greedy_modularity_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i + 1}: {community}")
