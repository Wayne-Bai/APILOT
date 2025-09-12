
import networkx as nx
G = nx.Graph()
# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')])
# Compute a minimum-weight maximal matching
matching = nx.algorithms.matching.max_weight_matching(G)
# Print the matching
print(matching)
