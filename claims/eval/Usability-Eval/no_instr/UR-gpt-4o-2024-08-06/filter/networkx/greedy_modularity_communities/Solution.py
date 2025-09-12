import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Create a sample graph
G = nx.karate_club_graph()

# Find communities using greedy modularity maximization
communities = greedy_modularity_communities(G)

# Print the communities
print([list(community) for community in communities])
