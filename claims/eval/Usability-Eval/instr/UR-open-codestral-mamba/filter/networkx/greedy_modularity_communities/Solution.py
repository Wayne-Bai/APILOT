import networkx as nx
import community as community_louvain

def find_communities(graph):
    # the communitization function will return a dictionary where the keys are node labels and the values are their corresponding community label
    community_dict = community_louvain.best_partition(graph)
    communities = set(community_dict.values())
    return communities, community_dict

# Create an example graph
G=nx.erdos_renyi_graph(100,0.01)

communities, community_dict = find_communities(G)
print(f"Found {len(communities)} communities.")
