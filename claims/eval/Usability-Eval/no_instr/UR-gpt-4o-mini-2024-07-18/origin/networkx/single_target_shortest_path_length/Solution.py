import networkx as nx

def compute_shortest_path_lengths(graph, target_node):
    # Ensure the target node exists in the graph
    if target_node not in graph:
        raise ValueError("Target node not found in the graph.")

    # Compute shortest path lengths from all reachable nodes to the target node
    shortest_path_lengths = nx.single_source_shortest_path_length(graph.reverse(), target_node)

    return shortest_path_lengths

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4)])
# target = 3
# lengths = compute_shortest_path_lengths(G, target)
# print(lengths)
