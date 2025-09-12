import networkx as nx
from networkx.algorithms.community import label_propagation_communities

# Create a graph
G = nx.karate_club_graph()

# Perform label propagation algorithm to find communities
community_list = list(label_propagation_communities(G))

# Print community sets
for i, community in enumerate(community_list):
    print(f"Community {i+1}: {community}")
