import networkx as nx

def generate_unique_node_label(graph, base_label):
    """Generate a unique node label that is not already in the graph."""
    unique_label = base_label
    counter = 1
    
    while unique_label in graph.nodes:
        unique_label = f"{base_label}_{counter}"
        counter += 1
    
    return unique_label

# Example usage
G = nx.Graph()
G.add_node("node_1")
new_label = generate_unique_node_label(G, "node")
print(new_label)  # Output will be "node_2" since "node_1" exists
