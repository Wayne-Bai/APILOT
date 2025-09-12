import networkx as nx
import random

def dual_barabasi_albert_graph(n, m1, m2, p, seed=None):
    """Returns a random graph using dual Barabási–Albert preferential attachment.

    Parameters:
    n (int): Number of nodes
    m1 (int): Number of edges to attach from a new node to existing nodes for the first model
    m2 (int): Number of edges to attach from a new node to existing nodes for the second model
    p (float): Probability of choosing the first model
    seed (int, optional): Seed for random number generator

    Returns:
    G (Graph): A random graph using dual Barabási–Albert preferential attachment
    """
    if seed is not None:
        random.seed(seed)

    G = nx.empty_graph(m1 + m2)
    repeated_nodes = list(G.nodes()) * (m1 + m2)

    for new_node in range(m1 + m2, n):
        if random.random() < p:
            # Use the first model
            targets = random.sample(repeated_nodes, m1)
        else:
            # Use the second model
            targets = random.sample(repeated_nodes, m2)

        G.add_node(new_node)
        for target in targets:
            G.add_edge(new_node, target)

        repeated_nodes += targets + [new_node] * (m1 + m2)

    return G

# Example usage:
# G = dual_barabasi_albert_graph(100, 2, 3, 0.5, seed=42)
