import networkx as nx

def google_matrix(G):
    """
    Returns the Google matrix of the graph.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    numpy.ndarray: The Google matrix of the graph.
    """
    # Get the number of nodes in the graph
    n = G.number_of_nodes()

    # Create a dictionary to store the transition probabilities
    P = {}

    # Calculate the transition probabilities for each node
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        degree = len(neighbors)
        P[node] = {neighbor: 1.0 / degree for neighbor in neighbors}

    # Create the Google matrix
    G_matrix = nx.from_dict_of_lists(P, create_using=nx.DiGraph())

    # Normalize the matrix
    row_sums = [sum(row) for row in G_matrix.adj.values()]
    for node in G_matrix.nodes():
        G_matrix.nodes[node]['weight'] = G_matrix.nodes[node]['weight'] / row_sums[node]

    return G_matrix
