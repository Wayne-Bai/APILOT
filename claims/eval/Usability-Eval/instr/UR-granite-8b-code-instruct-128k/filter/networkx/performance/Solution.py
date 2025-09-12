import networkx as nx

def partition_performance(G, partition):
    num_intra_community_edges = 0
    num_inter_community_non_edges = 0
    num_potential_edges = 0
    
    for node1, node2 in G.edges():
        if partition[node1] == partition[node2]:
            num_intra_community_edges += 1
        else:
            num_inter_community_non_edges += 1
            
        num_potential_edges += 1
        
    return (num_intra_community_edges + num_inter_community_non_edges) / num_potential_edges

G = nx.complete_graph(5)
partition = [0, 0, 1, 1, 1]
performance = partition_performance(G, partition)
print(performance)