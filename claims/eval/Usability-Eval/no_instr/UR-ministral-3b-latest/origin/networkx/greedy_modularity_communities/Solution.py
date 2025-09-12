import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Create an arbitrary graph
G = nx.erdos_renyi_graph(100, 0.1)  # Example graph with 100 nodes and an edge probability of 0.1

# Find communities using greedy modularity maximization
communities = greedy_modularity_communities(G)

print(communities)
