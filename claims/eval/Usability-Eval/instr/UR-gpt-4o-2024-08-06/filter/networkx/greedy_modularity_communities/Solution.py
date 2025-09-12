import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Example graph
G = nx.karate_club_graph()

# Finding communities using greedy modularity maximization
communities = greedy_modularity_communities(G)

# Convert the communities from a set of frozensets to a list of lists for easier handling/display
communities_list = [list(community) for community in communities]

# Display communities
for i, community in enumerate(communities_list, 1):
    print(f"Community {i}: {community}")
