import networkx as nx

# Example graph
G = nxipartite.Graph({('a', 'b'), ('b', 'c'), ('a', 'd'), ('d', 'c')})

# Compute the spectral ordering of the graph
def compute_spectral_ordering(graph):
    # Spectral ordering of the graph
    pos = nx.spring_layout(graph)
    ordering = nx.spectral_ordering(graph, pos)

    # Fetch the order
    order = [node for node, _ in ordering]

    return order

print(compute_spectral_ordering(G))
