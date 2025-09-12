
import networkx as nx

# Create a graph
G = nx.karate_club_graph()

# Use label propagation algorithm to detect communities
communities = nx_comm.label_propagation.label_propagation_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f'Community {i+1}: {community}')
