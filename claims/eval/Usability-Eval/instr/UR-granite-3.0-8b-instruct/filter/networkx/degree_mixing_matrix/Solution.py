import networkx as nx

def get_mixing_matrix(G, attribute):
    """
    This function returns the mixing matrix for the given attribute in the graph G.

    Parameters:
    G (networkx.Graph): The input graph.
    attribute (str): The attribute to calculate the mixing matrix for.

    Returns:
    numpy.ndarray: The mixing matrix.
    """
    # Get the attribute values for each node
    attr_values = {node: G.nodes[node][attribute] for node in G.nodes}

    # Create a dictionary to store the count of edges between nodes with different attribute values
    edge_counts = {}
    for edge in G.edges:
        u, v = edge
        if attr_values[u] != attr_values[v]:
            if (attr_values[u], attr_values[v]) not in edge_counts:
                edge_counts[(attr_values[u], attr_values[v])] = 0
            edge_counts[(attr_values[u], attr_values[v])] += 1

    # Create the mixing matrix
    mixing_matrix = nx.to_numpy_array(nx.DiGraph(), edge_counts.items())

    return mixing_matrix
