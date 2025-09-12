import networkx as nx

def compute_performance(graph, partition):
    intra_community_edges = 0
    inter_community_edges = 0

    for node in graph.nodes():
        node_community = partition[node]
        for neighbor in graph.neighbors(node):
            if partition[neighbor] == node_community:
                if graph.has_edge(node, neighbor):
                    intra_community_edges += 1
            else:
                if not graph.has_edge(node, neighbor):
                    inter_community_edges += 1

    total_potential_edges = graph.number_of_nodes() * (graph.number_of_nodes() - 1) / 2
    performance = (intra_community_edges + inter_community_edges) / total_potential_edges

    return performance

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 7), (7, 2)])
partition = {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1}

performance = compute_performance(G, partition)
print("Performance:", performance)
