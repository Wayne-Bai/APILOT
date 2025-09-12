import networkx as nx
import random

def barabasi_albert_graph(n, k):
    G = nx.Graph()
    G.add_nodes_from(range(n), degree=k)

    nodes_to_add = []
    for node in G.nodes:
        if G.degree(node) < k:
            nodes_to_add.append(node)

    while nodes_to_add:
        new_node = nodes_to_add.pop()
        G.add_node(new_node)
        G.add_edges_from((new_node, random.choice(list(G.neighbors(new_node)))))

    return G
