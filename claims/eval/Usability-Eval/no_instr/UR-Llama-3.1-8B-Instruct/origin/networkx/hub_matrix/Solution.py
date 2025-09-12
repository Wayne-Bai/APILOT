import networkx as nx
import numpy as np

def calculate_hubs(graph):
    """
    Calculate the HITS hub matrix.

    Parameters:
    graph (nx.Graph): The input graph.

    Returns:
    hubs (dict): A dictionary where the keys are the nodes and the values are their hub scores.
    authorities (dict): A dictionary where the keys are the nodes and the values are their authority scores.
    """
    hubs, authorities = nx.hits(graph)
    return hubs, authorities

# Example usage:
if __name__ == "__main__":
    # Create an example graph
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

    # Calculate the HITS hub matrix
    hubs, authorities = calculate_hubs(graph)

    # Print the result
    print("Hubs:", hubs)
    print("Authorities:", authorities)
