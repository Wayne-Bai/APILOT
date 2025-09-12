import networkx as nx

# Create a graph
G = nx.karate_club_graph()

# Find communities using the Clauset-Newman-Moore greedy modularity maximization
from networkx.algorithms.community import greedy_modularity_communities
communities = list(greedy_modularity_communities(G))

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i}: {sorted(community)}")
