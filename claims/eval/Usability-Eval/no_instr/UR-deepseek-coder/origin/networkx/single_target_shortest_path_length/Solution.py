import networkx as nx

def shortest_path_lengths_to_target(graph, target):
    shortest_paths = {}
    for node in graph.nodes():
        try:
            shortest_paths[node] = nx.shortest_path_length(graph, source=node, target=target)
        except nx.NetworkXNoPath:
            continue
    return shortest_paths

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
# target_node = 5
# result = shortest_path_lengths_to_target(G, target_node)
# print(result)
