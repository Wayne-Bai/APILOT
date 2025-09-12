import networkx as nx

def calculate_partition_performance(graph, partition):
    performance = 0
    for community in partition.values():
        community_graph = graph.subgraph(community)
        num_edges = community_graph.size()
        num_non_edges = len(community) * (len(community) - 1) // 2 - num_edges
        performance += num_edges + num_non_edges
    total_num_edges = graph.size()
    total_num_non_edges = len(graph) * (len(graph) - 1) // 2 - total_num_edges
    performance /= total_num_edges + total_num_non_edges
    return performance
