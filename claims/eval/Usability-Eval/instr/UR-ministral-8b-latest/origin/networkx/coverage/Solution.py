import networkx as nx

def calculate_coverage(graph):
    intra_community_edges = 0
    total_edges = len(graph.edges())

    for node in graph.nodes():
        neighbor_nodes = list(graph.neighbors(node))
        for neighboring_node in neighbor_nodes:
            if not graph.has_edge(neighboring_node, node):
                continue
            # Check if the neighboring nodes belong to the same community
            if all(graph.has_edge(neighboring_node, neighbor) for neighbor in neighbor_nodes):
                intra_community_edges += 1

    return intra_community_edges / total_edges

# Example usage
G = nx.Graph()
edges = [
    (0, 1), (1, 2), (2, 3),
    (3, 4), (4, 5), (5, 0),
    (0, 5), (1, 4), (2, 0),
    (3, 1), (4, 2), (5, 3)
]
G.add_edges_from(edges)
partition = {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5]}

coverage = calculate_coverage(G)
print(f"The coverage of the partition is: {coverage}")
