import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Generate a partition of the graph using the Louvain method
partition = nx.community.louvain_communities(G)

# Calculate the coverage and performance of the partition
coverage = len(partition) / len(G)
performance = sum(len(community) for community in partition) / len(G)

print(f"Coverage: {coverage}, Performance: {performance}")
