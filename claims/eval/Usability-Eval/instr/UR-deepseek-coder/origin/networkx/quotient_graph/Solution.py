import networkx as nx

def quotient_graph(G, partition):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx.Graph): The original graph.
    partition (list of sets): A list of sets representing the partition of the nodes.

    Returns:
    networkx.Graph: The quotient graph.
    """
    # Create a new graph for the quotient graph
    Q = nx.Graph()

    # Add nodes to the quotient graph, one for each set in the partition
    for part in partition:
        Q.add_node(tuple(part))

    # Add edges to the quotient graph based on the edges in the original graph
    for part1 in partition:
        for part2 in partition:
            if part1 != part2:
                # Check if there is any edge between nodes in part1 and part2
                for u in part1:
                    for v in part2:
                        if G.has_edge(u, v):
                            Q.add_edge(tuple(part1), tuple(part2))
                            break  # No need to check further for this pair of parts

    return Q

# Example usage:
# G = nx.complete_graph(4)
# partition = [{0, 1}, {2, 3}]
# Q = quotient_graph(G, partition)
# print(Q.edges())
