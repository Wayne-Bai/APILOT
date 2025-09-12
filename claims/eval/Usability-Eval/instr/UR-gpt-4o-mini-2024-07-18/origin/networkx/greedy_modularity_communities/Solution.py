import networkx as nx

def find_communities_with_greedy_modularity(G):
    # Use the Louvain method for community detection
    import community as community_louvain

    # Compute the best partition
    partition = community_louvain.best_partition(G)

    # Group nodes into communities
    communities = {}
    for node, comm in partition.items():
        if comm not in communities:
            communities[comm] = []
        communities[comm].append(node)

    return list(communities.values())

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (6, 7)])

    # Find communities
    communities = find_communities_with_greedy_modularity(G)
    print(communities)
