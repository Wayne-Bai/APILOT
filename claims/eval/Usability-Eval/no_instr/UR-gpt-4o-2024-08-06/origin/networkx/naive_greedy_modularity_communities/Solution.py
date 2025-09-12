import networkx as nx

def find_communities_greedy_modularity(G):
    """
    Finds communities in a graph using the greedy modularity maximization method.
    
    Parameters:
    G (networkx.Graph): The graph for which to find communities.

    Returns:
    list of sets: A list of communities, each represented as a set of nodes.
    """
    from networkx.algorithms.community import greedy_modularity_communities
    
    # Find communities
    communities = greedy_modularity_communities(G)
    
    # Convert to list of sets for compatibility with other analyses
    communities_list = [set(community) for community in communities]
    
    return communities_list

if __name__ == "__main__":
    # Example usage
    G = nx.karate_club_graph()
    communities = find_communities_greedy_modularity(G)
    print("Communities found:")
    for i, community in enumerate(communities):
        print(f"Community {i+1}: {community}")
