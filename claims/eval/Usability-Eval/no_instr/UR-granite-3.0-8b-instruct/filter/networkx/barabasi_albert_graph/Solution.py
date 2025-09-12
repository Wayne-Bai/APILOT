import networkx as nx

def generate_barabasi_albert_graph(n, m):
    """
    Generate a Barabási–Albert preferential attachment graph with n nodes and m edges.

    Parameters:
    n (int): The number of nodes in the graph.
    m (int): The number of edges to add at each time step.

    Returns:
    nx.Graph: The generated graph.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Add m edges to the graph at each time step
    for _ in range(m):
        new_node = n
        G.add_node(new_node)
        neighbors = [node for node in G.nodes if nx.degree(G, node) > 0]
        if len(neighbors) > 0:
            neighbor = random.choice(neighbors)
            G.add_edge(new_node, neighbor)
        else:
            break

    return G
