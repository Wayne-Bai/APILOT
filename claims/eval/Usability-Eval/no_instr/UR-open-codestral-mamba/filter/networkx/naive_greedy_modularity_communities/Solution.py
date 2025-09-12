import networkx as nx

# Initialize a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)
G.add_edge(5, 7)
G.add_edge(6, 7)
G.add_edge(6, 8)

# Find communities using greedy modularity maximization
communities = list(nx.community.greedy_modularity_communities(G))

# Print the communities
for i, comm in enumerate(communities):
    print(f"Community {i + 1}: {comm}")
