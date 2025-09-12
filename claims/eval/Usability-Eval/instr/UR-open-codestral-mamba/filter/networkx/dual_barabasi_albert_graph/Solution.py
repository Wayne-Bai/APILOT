import networkx as nx
import random

def dual_barabasi_albert_graph(n, m, p):
    """
    Generate a dual Barabási–Albert random graph.
    """
    # Start with an empty graph
    G = nx.empty_graph(m)

    # Add each node
    for i in range(m, n):
        # Edges are (u, v, {'is_ba': boolean})
        edges = []

        # Add m edges as in a regular BA
        degrees = [d for n, d in G.degree()]
        choices = zip(range(i), degrees)
        for u, degree in random.choices(choices, k=m):
            edges.append((u, i, {'is_ba': True}))

        # Add additional edges to old nodes
        for j in range(i):
            if random.random() < p:  # with probability p
                edges.append((j, i, {'is_ba': False}))

        # Add node with its edges
        G.add_edges_from(edges)

    return G
