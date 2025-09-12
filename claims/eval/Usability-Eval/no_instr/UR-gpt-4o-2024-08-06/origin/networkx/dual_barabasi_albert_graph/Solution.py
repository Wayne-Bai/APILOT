import networkx as nx
import random

def dual_barabasi_albert_graph(n, m1, m2, p):
    """
    Generate a dual Barabási–Albert graph.
    n: Number of nodes
    m1: Number of edges to attach from a new node to existing nodes for the first rule
    m2: Number of edges to attach from a new node to existing nodes for the second rule
    p: Probability of choosing the first rule over the second one for each node attachment
    """
    if m1 < 1 or m1 >= n:
        raise nx.NetworkXError("m1 must be greater than zero and less than n")
    if m2 < 1 or m2 >= n:
        raise nx.NetworkXError("m2 must be greater than zero and less than n")
    if not (0 <= p <= 1):
        raise nx.NetworkXError("p must be a probability between 0 and 1 inclusive")

    G = nx.empty_graph(m1)
    targets = list(range(m1))
    repeated_nodes = []

    source = m1
    while source < n:
        if random.random() < p:
            # Use rule with m1 edges
            new_targets = _pick_targets(G, m1, repeated_nodes)
        else:
            # Use rule with m2 edges
            new_targets = _pick_targets(G, m2, repeated_nodes)

        G.add_edges_from((source, target) for target in new_targets)
        repeated_nodes.extend(new_targets)
        repeated_nodes.extend([source] * (m1 if len(new_targets) == m1 else m2))

        source += 1

    return G

def _pick_targets(G, m, repeated_nodes):
    targets = set()
    while len(targets) < m:
        x = random.choice(repeated_nodes)
        targets.add(x)
    return targets

# Example usage:
n = 100  # Total number of nodes
m1 = 2  # Number of edges to attach, first preferential rule
m2 = 3  # Number of edges to attach, second preferential rule
p = 0.5  # Probability to follow the first rule

G = dual_barabasi_albert_graph(n, m1, m2, p)
print("Graph with", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")
