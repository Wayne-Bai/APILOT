import networkx as nx

# Let's assume that G is your graph
# If you don't already have a graph, create one as follows:
# G = nx.Graph()

# For (u, v, w) in E: # E is list of edges and weights
#     G.add_edge(u, v, weight=w)

# Compute a minimum-weight maximal matching in the graph
matching = nx.max_weight_matching(G, maxcardinality=True)

# The matching is a dictionary of nodes to their matches.
# For example, matching[1] would return the node that node 1 is matched with.
# If a node is not matched, it is not in the dictionary.
print(matching)
