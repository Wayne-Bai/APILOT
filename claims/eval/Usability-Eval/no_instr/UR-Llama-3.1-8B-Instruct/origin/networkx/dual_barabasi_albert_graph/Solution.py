import networkx as nx
import numpy as np

def generate_dual_barabasi_albert_graph(num_nodes, num_links):
    """
    Generates a graph using dual Barabási–Albert preferential attachment model.

    Parameters:
    num_nodes (int): Number of nodes to generate.
    num_links (int): Number of edges to introduce in the network.

    Returns:
    G (DiGraph): A directed graph.

    """
    G = nx.DiGraph()  # Create an empty directed graph.
    G.add_nodes_from(range(num_nodes))  # Add nodes to the graph.

    # Start with an empty graph and add nodes one by one.
    for i in range(num_nodes):
        # List of existing nodes in the graph.
        existing_nodes = list(G.nodes())

        # If this is not the first node, add edges from this node to some existing nodes.
        if i > 0:
            # For each edge we want to add, select a target node based on the degree of the nodes.
            for _ in range(2):
                # Select a random target node from the existing nodes based on the degree.
                j = np.random.choice(existing_nodes, p=[G.degree(n) for n in existing_nodes], size=1)[0]
                G.add_edge(i, j)

        # For the two edges we need to introduce by the formula, choose their target nodes based on the degree.
        targets1 = np.random.choice(existing_nodes, p=[G.degree(n) for n in existing_nodes], size=1)[0]
        targets2 = np.random.choice(existing_nodes, p=[G.degree(n) for n in existing_nodes], size=1)[0]

        G.add_edge(i, targets1)
        G.add_edge(i, targets2)

    # Now we add the edges we want.
    existing_nodes = list(G.nodes())
    for i in range(num_nodes):
        for _ in range(num_links):
            j = np.random.choice(existing_nodes, p=[G.degree(n) for n in existing_nodes], size=1)[0]
            # If a self-loop or a multiple edge is created, remove it.
            if i!= j:
                G.add_edge(i, j)

    return G

# Generate a graph with 100 nodes and 100 links
G = generate_dual_barabasi_albert_graph(100, 100)
