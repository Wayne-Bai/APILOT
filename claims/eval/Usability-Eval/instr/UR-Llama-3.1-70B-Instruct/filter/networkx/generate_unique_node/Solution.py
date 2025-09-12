import networkx as nx

def generate_unique_node_label(G, prefix='node'):
    """
    Generate a unique node label for a graph.

    Parameters:
    G (networkx.Graph): The input graph.
    prefix (str): The prefix for the node label. Default is 'node'.

    Returns:
    str: A unique node label.
    """
    nodes = list(G.nodes())
    if not nodes:
        return f"{prefix}_0"
    node_labels = [node for node in nodes if str(node).startswith(prefix)]
    if not node_labels:
        return f"{prefix}_0"
    node_numbers = [int(node.split('_')[1]) for node in node_labels]
    max_number = max(node_numbers)
    return f"{prefix}_{max_number + 1}"

# Create an empty graph
G = nx.Graph()

# Generate a unique node label
unique_label = generate_unique_node_label(G)
print(unique_label)  # Output: node_0

# Add the unique node label to the graph
G.add_node(unique_label)

# Generate another unique node label
unique_label = generate_unique_node_label(G)
print(unique_label)  # Output: node_1
