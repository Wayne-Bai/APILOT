import networkx as nx

def generate_communities(graph):
    # Generate communities using the Label Propagation Algorithm
    communities = nx.algorithms.community.label_propagation.label_propagation_communities(graph)

    return communities

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.karate_club_graph()

    # Generate community sets
    communities = generate_communities(G)

    # Print communities
    for i, community in enumerate(communities):
        print(f"Community {i}: {community}")
