
import networkx as nx

def calculate_performance_of_partition(G, partition):
    intra_community_edges = 0
    inter_community_non_edges = 0
    
    for node1, node2 in G.edges():
        if partition[node1] == partition[node2]:
            intra_community_edges += 1
        else:
            if not G.has_edge(node1, node2):
                inter_community_non_edges += 1
    
    total_potential_edges = len(G.edges())
    performance = (intra_community_edges + inter_community_non_edges) / total_potential_edges

    return performance

# Example of how to use the function
G = nx.karate_club_graph()
partition = {node: node%2 for node in G.nodes()}  # Example partition - nodes are divided into two communities
performance = calculate_performance_of_partition(G, partition)
print("Performance of the partition:", performance)
