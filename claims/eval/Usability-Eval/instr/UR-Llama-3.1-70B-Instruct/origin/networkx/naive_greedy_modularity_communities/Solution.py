import networkx as nx
import community

# Generate a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

# Find communities in G using greedy modularity maximization
partition = community.best_partition(G)

# Print community assignments for each node
for node, community_id in partition.items():
    print(f"Node: {node}, Community: {community_id}")

# Calculate modularity of the partition
modularity = community.modularity(partition, G)
print(f"Modularity: {modularity}")
