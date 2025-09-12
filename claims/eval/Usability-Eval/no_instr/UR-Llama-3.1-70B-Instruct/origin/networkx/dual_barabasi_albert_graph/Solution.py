import networkx as nx
import matplotlib.pyplot as plt
import random

def random_graph_dual_barabasi_albert(n, m1, m2, seed=None):
    """
    Returns a random graph using dual Barabási–Albert preferential attachment.

    Parameters:
    n (int): The number of nodes in the graph.
    m1 (int): The number of edges each new node is connected to in the first round.
    m2 (int): The number of edges each new node is connected to in the second round.
    seed (int): Optional, seed for random number generation.

    Returns:
    G (nx.Graph): A random graph using dual Barabási–Albert preferential attachment.
    """
    if seed is not None:
        random.seed(seed)
        nx.random.seed(seed)

    # Create a new directed graph
    G = nx.Graph()

    # Add the first m1 nodes
    nodes = list(range(m1))
    G.add_nodes_from(nodes)

    # Connect the nodes to each other
    for i in range(m1):
        for j in range(i+1, m1):
            if random.random() < 0.5:
                G.add_edge(nodes[i], nodes[j])

    # Add the rest of the nodes
    for i in range(m1, n):
        G.add_node(i)
        # Connect to m1 existing nodes
        for j in random.sample(list(range(i)), min(m1, i)):
            G.add_edge(i, j)
        # Connect to m2 existing nodes
        for j in random.sample(list(range(i)), min(m2, i)):
            if random.random() < 0.5:  # Avoid duplicate edges
                if not G.has_edge(i, j):
                    G.add_edge(i, j)

    return G

# Example usage
G = random_graph_dual_barabasi_albert(10, 2, 2, seed=42)

# Print the graph nodes and edges
print("Nodes: ", G.nodes())
print("Edges: ", G.edges())

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
