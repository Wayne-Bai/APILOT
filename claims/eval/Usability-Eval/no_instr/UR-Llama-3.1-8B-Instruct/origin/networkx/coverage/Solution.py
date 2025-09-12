import networkx as nx
import numpy as np

def calculate_coverage(graph, partition):
    """
    Calculate the coverage of a partition.

    Parameters:
    graph (nx.Graph): The input graph.
    partition (dict): A partition of the graph where each key is a node and its value is the community it belongs to.

    Returns:
    float: The coverage of the partition.
    """
    # Calculate the total number of edges in the graph
    total_edges = graph.number_of_edges()

    # Initialize a list to store intra-community edges
    intra_community_edges = 0

    # Iterate over each community in the partition
    for community in set(partition.values()):
        # Create a subgraph for the current community
        community_graph = graph.subgraph([node for node, com in partition.items() if com == community])

        # Update intra_community_edges with the number of edges in the subgraph
        intra_community_edges += community_graph.number_of_edges()

    # Calculate the coverage of the partition
    if total_edges == 0:
        coverage = 0
    else:
        coverage = intra_community_edges / total_edges

    return coverage


# Example usage:
if __name__ == "__main__":
    # Generate a sample graph
    G = nx.Graph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('B', 'C')
    G.add_edge('B', 'D')
    G.add_edge('C', 'D')
    G.add_edge('E', 'F')

    # Assign a partition to the graph nodes
    partition = {'A': 'community1', 'B': 'community1', 'C': 'community1', 'D': 'community1', 'E': 'community2', 'F': 'community2'}

    # Calculate the coverage of the partition
    coverage = calculate_coverage(G, partition)

    print("Coverage of the partition:", coverage)
