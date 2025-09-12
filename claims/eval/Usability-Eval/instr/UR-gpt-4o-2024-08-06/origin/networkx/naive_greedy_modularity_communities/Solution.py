import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Create a graph G (Example graph)
G = nx.karate_club_graph()

# Use the greedy modularity maximization method to find communities
communities = greedy_modularity_communities(G)

# Convert community data into a more readable format and display
community_list = [list(community) for community in communities]
print("Communities found using greedy modularity maximization:")
for i, community in enumerate(community_list, start=1):
    print(f"Community {i}: {community}")
