import networkx as nx

def label_propagation_community_detection(graph):
    communities = nx.algorithms.community.label_propagation_communities(graph)
    return list(communities)

# Example usage:
G = nx.karate_club_graph()
result = label_propagation_community_detection(G)
print("Detected Communities:", list(result))
