import networkx as nx

def quotient_graph(G, partition):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx.Graph): The original graph.
    partition (list of sets): A list of sets where each set represents a partition of the nodes.

    Returns:
    networkx.Graph: The quotient graph.
    """
    # Create a new graph for the quotient graph
    Q = nx.Graph()

    # Add nodes to the quotient graph, one for each partition
    for part in partition:
        Q.add_node(tuple(part))

    # Add edges to the quotient graph based on the edges between partitions in the original graph
    for part1 in partition:
        for part2 in partition:
            if part1 != part2:
                edges = []
                for node1 in part1:
                    for node2 in part2:
                        if G.has_edge(node1, node2):
                            edges.append((node1, node2))
                if edges:
                    Q.add_edge(tuple(part1), tuple(part2), weight=len(edges))

    return Q

# Example usage:
# G = nx.complete_graph(5)
# partition = [{0, 1}, {2, 3}, {4}]
# Q = quotient_graph(G, partition)
# print(Q.edges(data=True))
