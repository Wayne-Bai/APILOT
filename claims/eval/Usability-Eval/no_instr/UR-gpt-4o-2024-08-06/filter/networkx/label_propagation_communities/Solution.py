import networkx as nx

def label_propagation_communities(G):
    """
    Detects communities in graph G using the label propagation algorithm.

    Parameters:
    G (networkx.Graph): The graph on which to perform community detection.

    Returns:
    list: A list where each element is a set containing the nodes in one community.
    """
    communities_generator = nx.algorithms.community.label_propagation_communities(G)
    communities = [set(community) for community in communities_generator]
    return communities

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.erdos_renyi_graph(n=10, p=0.5)

    # Detect communities
    communities = label_propagation_communities(G)
    
    # Print the communities
    for index, community in enumerate(communities):
        print(f"Community {index + 1}: {community}")
