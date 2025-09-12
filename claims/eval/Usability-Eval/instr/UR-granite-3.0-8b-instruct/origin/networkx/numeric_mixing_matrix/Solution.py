import networkx as nx

def get_mixing_matrix(graph, attribute):
    """
    Returns numeric mixing matrix for attribute.

    Parameters:
    graph (nx.Graph): The graph to calculate the mixing matrix for.
    attribute (str): The attribute to use for the mixing matrix.

    Returns:
    numpy.ndarray: The mixing matrix.
    """
    # Get the nodes with the specified attribute
    nodes = [node for node in graph.nodes if graph.nodes[node].get(attribute) is not None]

    # Get the attribute values for each node
    attribute_values = [graph.nodes[node].get(attribute) for node in nodes]

    # Create a dictionary to map attribute values to indices
    value_to_index = {value: index for index, value in enumerate(set(attribute_values))}

    # Create a list of lists to represent the mixing matrix
    mixing_matrix = [[0] * len(value_to_index) for _ in range(len(value_to_index))]

    # Iterate over the edges in the graph
    for source, target in graph.edges():
        # Get the attribute values for the source and target nodes
        source_value = graph.nodes[source].get(attribute)
        target_value = graph.nodes[target].get(attribute)

        # Increment the appropriate cell in the mixing matrix
        mixing_matrix[value_to_index[source_value]][value_to_index[target_value]] += 1

    # Normalize the mixing matrix
    row_sums = [sum(row) for row in mixing_matrix]
    for i in range(len(mixing_matrix)):
        mixing_matrix[i] = [value / row_sums[i] for value in mixing_matrix[i]]

    return nx.to_numpy_array(mixing_matrix)
