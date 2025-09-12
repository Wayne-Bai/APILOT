import networkx as nx
import numpy as np

def random_dual_ba_graph(n, m, seed=None):
    """
    Generate a random graph using dual Barabási–Albert preferential attachment.

    Parameters:
    n (int): Number of nodes in the graph.
    m (int): Number of edges to attach from a new node to existing nodes.
    seed (int, optional): Seed for the random number generator.

    Returns:
    networkx.Graph: The generated graph.
    """
    if seed is not None:
        np.random.seed(seed)

    # Create an empty graph
    G = nx.Graph()

    # Add the initial nodes
    G.add_nodes_mobile(n)

    # Create a list of nodes with their degrees
    nodes = list(G.nodes())
    degrees = [0] * n

    # Add edges using dual Barabási–Albert preferential attachment
    for _ in range(n - 1):
        new_node = nodes[-1]
        G.add_node(new_node)

        # Choose the m nodes with the highest degrees
        top_nodes = np.argsort(degrees)[-m:]

        # Add edges between the new node and the top nodes
        for node in top_nodes:
            G.add_edge(new_node, node)

        # Update the degrees of the top nodes
        for node in top_nodes:
            degrees[node] += 1

    return G
