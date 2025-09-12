
import networkx as nx

def coverage_performance(partition, G):
    coverage = 0
    performance = 0
    
    for nodes in partition:
        internal_edges = 0
        external_edges = 0
        
        for node1 in nodes:
            for node2 in nodes:
                if node1 != node2:
                    if G.has_edge(node1, node2):
                        internal_edges += 1
        
        for node in nodes:
            neighbors = set(G.neighbors(node))
            for neighbor in neighbors:
                if neighbor not in nodes:
                    external_edges += 1
        
        coverage += internal_edges
        performance += internal_edges / (internal_edges + external_edges)
    
    return coverage, performance
