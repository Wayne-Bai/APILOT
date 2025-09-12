import networkx as nx

def generate_unique_node_label(graph):
    """
    Generates a unique node label for a given graph.
    
    Parameters:
    graph (networkx.Graph): The graph to generate a unique node label for.
    
    Returns:
    str: A unique node label.
    """
    node_labels = set(graph.nodes())
    new_label = 0
    while str(new_label) in node_labels:
        new_label += 1
    return str(new_label)

# Example usage:
G = nx.Graph()
G.add_node('0')
G.add_node('1')
unique_label = generate_unique_node_label(G)
print(f"Unique node label: {unique_label}")
