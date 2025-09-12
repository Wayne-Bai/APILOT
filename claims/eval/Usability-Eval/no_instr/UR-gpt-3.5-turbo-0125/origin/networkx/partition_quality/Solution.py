
import networkx as nx

# Create a graph
G = nx.Graph()
# Add nodes and edges to the graph G
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Create a partition of the nodes
partition = [{1}, {2, 3}]

# Calculate coverage and performance of the partition
coverage = nx.community.coverage(G, partition)
performance = nx.community.performance(G, partition)

print("Coverage:", coverage)
print("Performance:", performance)
