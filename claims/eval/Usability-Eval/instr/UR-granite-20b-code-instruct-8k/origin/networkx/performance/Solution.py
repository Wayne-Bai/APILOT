import networkx as nx

def partition_performance(graph, partition):
    # Calculate the number of inter-community edges
    inter_community_edges = 0
    for community in partition.values():
        for node_1 in community:
            for node_2 in community:
                if node_1 != node_2 and graph.has_edge(node_1, node_2):
                    inter_community_edges += 1

    # Calculate the number of intra-community edges
    intra_community_edges = sum([graph.edges(community) for community in partition.values()])

    # Calculate the number of potential edges
    potential_edges = graph.number_of_nodes() * (graph.number_of_nodes() - 1) / 2

    # Calculate the performance of the partition
    performance = (intra_community_edges + inter_community_edges) / potential_edges

    return performance
