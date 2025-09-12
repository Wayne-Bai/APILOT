import networkx as nx

def generate_unique_node_label(graph, base_label):
    """
    Generate a unique node label for a given graph based on a base label.
    
    Parameters:
    graph (nx.Graph): The graph to which the label will be added.
    base_label (str): The base label to use for generating a unique label.
    
    Returns:
    str: A unique node label.
    """
    unique_label = base_label
    count = 1
    
    # Check for existing labels to ensure uniqueness
    while unique_label in graph.nodes:
        unique_label = f"{base_label}_{count}"
        count += 1
    
    return unique_label

# Example of usage
G = nx.Graph()
label = generate_unique_node_label(G, "Node")
G.add_node(label)
print(f"Added node with label: {label}")
