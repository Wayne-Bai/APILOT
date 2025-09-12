import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

# Find communities using greedy modularity maximization
communities = list(greedy_modularity_communities(G))

print(communities)
