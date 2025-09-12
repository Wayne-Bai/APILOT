import networkx as nx

def calculate_coverage(g, partition):
    num_nodes = g.number_of_nodes()
    total_num_edges = g.number_of_edges()

    intra_community_edges = sum([len(g.subgraph([p]).edges()) for p in partition])

    coverage = intra_community_edges / total_num_edges
    return coverage

# Example usage
G = nx.karate_club_graph()
partition = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12]  # Example partition

coverage = calculate_coverage(G, partition)
print(coverage)
