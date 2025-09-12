import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Create a sample graph (replace with your own graph)
G = nx.erdos_renyi_graph(n=100, p=0.05)

# Find communities using greedy modularity maximization
communities = greedy_modularity_communities(G)

# Convert the communities to a list of sets for easier interpretation
community_list = [set(community) for community in communities]

# Print the communities
for i, community in enumerate(community_list):
    print(f"Community {i+1}: {community}")
