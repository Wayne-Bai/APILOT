import networkx as nx

def dual_barabasi_albert_graph(n, m, p, seed=None):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if i < n / 2:
                if random.random() < p:
                    G.add_edge(i, j)
            else:
                if random.random() < p / 2:
                    G.add_edge(i, j)
    return G
