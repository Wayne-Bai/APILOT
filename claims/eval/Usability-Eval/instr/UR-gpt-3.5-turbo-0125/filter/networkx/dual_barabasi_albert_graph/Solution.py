
import networkx as nx
import random

def dual_barabasi_albert_graph(n, m, p, q):
    G = nx.Graph()
    G.add_edge(0, 1)
    
    for i in range(2, n):
        for j in range(m):
            if random.random() < p:
                existing_nodes = list(G.nodes)
                new_node = existing_nodes[random.randint(0, len(existing_nodes)-1)]
                G.add_edge(i, new_node)
            else:
                existing_edges = list(G.edges)
                new_edge = existing_edges[random.randint(0, len(existing_edges)-1)]
                G.add_edge(i, new_edge[0] if random.random() < q else new_edge[1])
    
    return G
