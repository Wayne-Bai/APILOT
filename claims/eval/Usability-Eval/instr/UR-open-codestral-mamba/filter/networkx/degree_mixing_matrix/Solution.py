import networkx as nx

def get_mixing_matrix(graph, attribute):
    nodes = graph.nodes()
    N = len(nodes)

    mixing_matrix = nx.to_numpy_matrix(graph, nodelist=nodes)

    for i in range(N):
        for j in range(N):
            attr_i = graph.nodes[nodes[i]][attribute]
            attr_j = graph.nodes[nodes[j]][attribute]
            mixing_matrix[i, j] = mixing_matrix[i, j] * attr_i * attr_j

    return mixing_matrix
