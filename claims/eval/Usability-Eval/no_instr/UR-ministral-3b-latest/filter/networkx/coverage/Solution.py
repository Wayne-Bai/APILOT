import networkx as nx

def calculate_partition_coverage(G, partition):
    intra_community_edges = 0
    total_edges = 0

    for node in G.nodes():
        if G.degree(node) > 0:
            total_edges += G.degree(node)
            for neighbor in G.neighbors(node):
                if G.edges[node, neighbor] in partition:
                    intra_community_edges += 1

    if total_edges == 0:
        return 0.0

    return intra_community_edges / total_edges

# Example graph
G = nx.erdos_renyi_graph(10, 0.2)

# Example partition (assuming it returns a list of edges)
partition = [(node1, node2) for node1, node2 in edge_list if condition]

coverage = calculate_partition_coverage(G, partition)
coverage
