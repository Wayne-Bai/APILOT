import networkx as nx

def calculate_coverage(graph):
    # Compute the total number of edges in the graph
    total_edges = graph.number_of_edges()

    # Compute the number of intra-community edges
    # This is done by iterating through the connected components of the graph
    intra_community_edges = 0
    for component in nx.connected_components(graph):
        subgraph = graph.subgraph(component)
        intra_community_edges += subgraph.number_of_edges()

    # Compute and return the coverage
    coverage = intra_community_edges / total_edges
    return coverage

# Example usage:
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

print(calculate_coverage(G))
