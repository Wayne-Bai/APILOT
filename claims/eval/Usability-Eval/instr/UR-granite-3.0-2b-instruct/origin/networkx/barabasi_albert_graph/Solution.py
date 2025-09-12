import networkx as nx
import numpy as np

def generate_barabasi_albert_graph(n_nodes, m_edges):
    G = nx.Graph()
    G.add_nodes_from(range(n_nodes))

    nodes_with_connections = []
    for _ in range(m_edges):
        new_node = np.random.randint(0, n_nodes)
        G.add_edge(nodes_with_connections[-1], new_node)
        nodes_with_connections.append(new_node)

    return G
