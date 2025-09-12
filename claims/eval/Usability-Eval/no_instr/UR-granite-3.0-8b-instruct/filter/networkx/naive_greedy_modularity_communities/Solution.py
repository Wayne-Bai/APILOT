import networkx as nx

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

print(communities)
