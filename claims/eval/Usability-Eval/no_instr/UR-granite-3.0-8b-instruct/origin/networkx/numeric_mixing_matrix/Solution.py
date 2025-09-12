import networkx as nx

def mixing_matrix(G, attribute):
    """
    Returns the numeric mixing matrix for the given attribute.

    Parameters:
    G (networkx.Graph): The graph to calculate the mixing matrix for.
    attribute (str): The attribute to use for the mixing matrix.

    Returns:
    numpy.ndarray: The mixing matrix.
    """
    # Get the attribute values for each node
    attribute_values = [G.nodes[node][attribute] for node in G.nodes]

    # Create a dictionary to map attribute values to indices
    attribute_map = {value: index for index, value in enumerate(set(attribute_values))}

    # Create a matrix to store the mixing matrix
    mixing_matrix = nx.empty_matrix(len(G), len(G), dtype=int)

    # Iterate over each edge in the graph
    for u, v, attr in G.edges(data=True):
        # Get the attribute values for the nodes
        u_attr = G.nodes[u][attribute]
        v_attr = G.nodes[v][attribute]

        # Get the indices for the attribute values
        u_index = attribute_map[u_attr]
        v_index = attribute_map[v_attr]

        # Increment the count for the corresponding cell in the matrix
        mixing_matrix[u_index, v_index] += 1

    # Normalize the matrix by dividing each cell by the total number of edges
    total_edges = sum(mixing_matrix.sum(axis=0))
    mixing_matrix = mixing_matrix / total_edges

    return mixing_matrix
