
import networkx as nx

# Define the Graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'E')])

# Define the partition
parts = [['A', 'B'], ['C', 'D', 'E']]

# Compute the coverage and performance of the partition
coverage = nx.partition_coverage(G, parts)
performance = nx.partition_performance(G, parts)

print("Coverage:", coverage)
print("Performance:", performance)
