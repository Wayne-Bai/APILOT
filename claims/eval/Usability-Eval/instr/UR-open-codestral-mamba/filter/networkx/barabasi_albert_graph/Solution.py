import networkx as nx

def generate_random_graph(n, m):
    """
    This function generates a random graph using the Barabási–Albert preferential attachment model.

    Parameters:
    n (int): The number of nodes in the generated graph.
    m (int): The number of edges to attach from a new node to existing nodes in the graph.
    """
    G = nx.empty_graph(m)  # start with m nodes (a line)
    G.add_edges_from([(i, i + 1) for i in range(m - 1)])

    for i in range(m, n):
        # Add the new node and connect it to m random existing nodes
        G.add_node(i)
        for _ in range(m):
            G.add_edge(i, G.nodes[nx.utils.discrete_sequence(1, source=m, stop=i)])

    return G
