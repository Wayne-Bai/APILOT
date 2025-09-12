import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (5, 7), (6, 7)])

# Find communities using greedy modularity maximization
communities = list(greedy_modularity_communities(G))

print(communities)
