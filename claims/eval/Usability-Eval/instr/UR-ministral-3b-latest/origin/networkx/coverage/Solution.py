import networkx as nx
def calculate_coverage(graph):
    total_edges = len(graph.edges)
    intra_community_edges = sum(len(community.edges) for community in nx.strongly_connected_components(graph))
    coverage = intra_community_edges / total_edges
    return coverage

# Example usage:
# G = nx.karate_club_graph()
# print(calculate_coverage(G))
