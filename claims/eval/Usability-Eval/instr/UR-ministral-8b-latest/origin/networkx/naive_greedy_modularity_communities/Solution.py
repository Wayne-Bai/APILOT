import networkx as nx
from community import community_louvain

# Create an example graph
G = nx.karate_club_graph()

# Compute the communities using the Louvain method
partition = community_louvain.best_partition(G)

# Print the communities
for node in G.nodes():
    print(f"Node {node} is in community {partition[node]}")
