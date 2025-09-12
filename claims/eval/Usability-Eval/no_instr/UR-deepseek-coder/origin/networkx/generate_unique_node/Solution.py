import networkx as nx

def generate_unique_node_label(graph):
    """
    Generate a unique node label for the given graph.

    Parameters:
    graph (networkx.Graph): The graph to which the node label will be added.

    Returns:
    str: A unique node label.
    """
    node_labels = set(graph.nodes())
    counter = 1
    while f"node_{counter}" in node_labels:
        counter += 1
    return f"node_{counter}"

# Example usage:
G = nx.Graph()
unique_label = generate_unique_node_label(G)
print(unique_label)
