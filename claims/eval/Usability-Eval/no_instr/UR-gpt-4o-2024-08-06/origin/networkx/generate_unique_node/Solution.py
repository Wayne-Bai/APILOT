import networkx as nx

def generate_unique_node_label(graph, base_label='node'):
    """
    Generates a unique node label for a given graph by appending a number to the base label.

    Parameters:
    - graph (nx.Graph): The graph to which the node will be added.
    - base_label (str): The base label to use for generating the unique node label.

    Returns:
    - str: A unique node label.
    """
    i = 1
    while True:
        potential_label = f"{base_label}_{i}"
        if potential_label not in graph:
            return potential_label
        i += 1

# Example usage:
G = nx.Graph()
new_node_label = generate_unique_node_label(G)
G.add_node(new_node_label)
print(f"New node added with label: {new_node_label}")
