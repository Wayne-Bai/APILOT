import networkx as nx
from networkx.algorithms.community import label_propagation_communities

# Example graph creation
G = nx.karate_club_graph()

# Using label propagation for community detection
communities = list(label_propagation_communities(G))

# Print the detected communities
for community in communities:
    print(community)
