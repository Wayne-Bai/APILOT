import networkx as nx

# Assuming G is your graph
G = nx.karate_club_graph()  # Example graph, replace with your graph

# Find communities using greedy modularity maximization
communities = nx.algorithms.community.greedy_modularity_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i+1}: {list(community)}")
