import networkx as nx
import random

def dual_barabasi_albert_graph(n, m, p):
    """
    Generates a dual Barabási–Albert graph.

    Parameters:
    n (int): Number of nodes in the graph.
    m (int): Number of edges to attach from a new node to existing nodes.
    p (float): Probability for creating a new node that connects to an existing node.

    Returns:
    Graph: A random dual Barabási–Albert graph.
    """
    if m < 1 or m >= n:
        raise ValueError("m must be at least 1 and less than n")

    # Create an initial complete graph with m nodes
    G = nx.complete_graph(m)

    # List of existing nodes
    existing_nodes = list(G.nodes())
    
    # Adding new nodes to the graph
    for i in range(m, n):
        new_node = i
        G.add_node(new_node)

        # Attach m edges to existing nodes preferentially
        targets = set()
        while len(targets) < m:
            if random.random() < p:
                # Connection to existing nodes with probability p
                targets.add(random.choice(existing_nodes))
            else:
                # Connection to a random node
                targets.add(random.choice(existing_nodes + [new_node]))  # include new_node for additional randomness
        
        for target in targets:
            G.add_edge(new_node, target)

        existing_nodes.append(new_node)

    return G

# Example usage
n = 100  # Number of nodes
m = 3    # Number of edges to attach
p = 0.5  # Probability for a random connection
graph = dual_barabasi_albert_graph(n, m, p)
