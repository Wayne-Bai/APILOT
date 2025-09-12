import networkx as nx

def compute_shortest_path_lengths(graph, target):
    # Compute the shortest path lengths from all reachable nodes to the target
    shortest_path_lengths = nx.single_source_shortest_path_length(graph.reverse(), target)
    return shortest_path_lengths

# Example usage:
if __name__ == "__main__":
    # Create a directed graph
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)])

    target_node = 4
    lengths = compute_shortest_path_lengths(G, target_node)
    print(lengths)  # Output the lengths from reachable nodes to the target
