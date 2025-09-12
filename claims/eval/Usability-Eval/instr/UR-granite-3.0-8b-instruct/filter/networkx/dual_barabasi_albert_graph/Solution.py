import networkx as nx
import random

def random_graph_ba(n, m0):
    G = nx.Graph()
    G.add_star([0] * m0)

    for node in range(m0, n):
        neighbors = random.choices(list(G.nodes()), weights=[G.degree(n) for n in G.nodes()])
        G.add_edges_from([(0, neighbor) for neighbor in neighbors])

    return G
