
import networkx as nx

def partition_coverage(graph, partition):
    intra_edges = 0
    total_edges = graph.number_of_edges()
    
    for comm_nodes in partition:
        comm_graph = graph.subgraph(comm_nodes)
        intra_edges += comm_graph.number_of_edges()
        
    coverage = intra_edges / total_edges
    return coverage
