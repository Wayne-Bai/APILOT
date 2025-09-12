import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G, max_iter=300, seed=42)

# Print the communities
for group in communities:
    print(f'Group: {group}', list(set(G.nodes[group])))
