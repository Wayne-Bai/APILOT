import networkx as nx

def avg_degree_connectivity(G):
    avg_conn = 0
    for node in G.nodes():
        k = G.degree(node)
        if k > 0:
            avg_conn += sum(G.neighbors(node)) / k
    return avg_conn / len(G.nodes())

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
print(avg_degree_connectivity(G))
