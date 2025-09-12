import networkx as nx

def triadic_census(graph, nodelist=None):
    if nodelist is not None:
        subgraph = graph.subgraph(nodelist)
    else:
        subgraph = graph

    triads = nx.triadic_census(subgraph)
    return triads

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3)])
# census = triadic_census(G, nodelist=[1, 2, 3])
# print(census)
