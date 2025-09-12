import networkx as nx
import random

def dual_barabasi_albert_graph(n, m1, m2, s1, s2, seed=None):
    if m1 == 0 or m2 == 0:
        raise nx.NetworkXError(
            "Both m1 and m2 must be greater than 0."
        )
    if s1 < 0 or s2 < 0:
        raise nx.NetworkXError(
            "Both s1 and s2 must be non-negative."
        )
    if s1 == 0 and s2 == 0:
        raise nx.NetworkXError(
            "At least one of s1 or s2 must be positive."
        )
    if (m1 + m2 + s1 + s2) / 2 > n:
        raise nx.NetworkXError(
            "The sum of m1, m2, s1, and s2 must be less than or equal to 2*n."
        )

    G=nx.empty_graph(n)

    # add nodes
    G.name="dual_barabasi_albert_graph{}".format(seed)
    if n==0 or (n==1 and (s1 > 0 or s2 > 0)):
        return G

    if s1 > 0:
        nodes = list(range(m1))
        G.add_edges_from(nx.empty_graph(n=m1), from_nodes=nodes)
        nodes = list(range(m1))
        for source in range(m1, n):
            targets = random.choices(nodes, k=s1)
            G.add_edges_from(zip([source]*s1, targets))
            nodes.extend(targets)

    if s2 > 0:
        nodes = list(range(n-m2, n))
        G.add_edges_from(nx.empty_graph(n=m2), from_nodes=nodes)
        nodes = list(range(n-m2, n))
        for source in range(n-m2-1, -1, -1):
            targets = random.choices(nodes, k=s2)
            G.add_edges_from(zip([source]*s2, targets))
            nodes.extend(targets)

    return G

# Example usage:
G = dual_barabasi_albert_graph(100, 5, 5, 2, 2)
