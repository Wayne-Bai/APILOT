import networkx as nx

def shortest_path_lengths_to_target(graph, target):
    # Ensure the target node is in the graph
    if target not in graph:
        raise ValueError("Target node is not in the graph")
    
    # Compute shortest path lengths for all reachable nodes to the target
    shortest_paths_to_target = {}
    
    # For each node in the graph, calculate the shortest path length to the target
    for node in graph.nodes:
        try:
            # Get the length of the shortest path from the node to the target using Dijkstra's algorithm
            length = nx.shortest_path_length(graph, source=node, target=target)
            # Add the length to the dictionary if a path exists
            shortest_paths_to_target[node] = length
        except nx.NetworkXNoPath:
            # If no path exists, skip this node
            pass
    
    return shortest_paths_to_target

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 5), (3, 5)])
target_node = 3
shortest_paths = shortest_path_lengths_to_target(G, target_node)
print(shortest_paths)
