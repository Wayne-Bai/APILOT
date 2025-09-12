import networkx as nx

def generate_barabasi_albert_graph(n, m):
    """
    Generate a random graph using Barabási–Albert preferential attachment.

    Parameters:
    n (int): The number of nodes in the graph.
    m (int): The number of edges to attach from a new node to existing nodes.

    Returns:
    nx.Graph: The generated random graph.
    """
    # Create an empty graph
    G = nx.Graph()

    # Add n nodes to the graph
    G.add_nodes_from(range(n))

    # Add m edges to the graph using preferential attachment
    for _ in range(m):
        new_node = n
        G.add_node(new_node)
        for node in G.nodes():
            if nx.number_of_edges(G, node) < m:
                G.add_edge(new_node, node)
                break

    return G
