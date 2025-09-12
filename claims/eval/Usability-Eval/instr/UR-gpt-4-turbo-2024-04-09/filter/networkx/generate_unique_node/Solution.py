import networkx as nx

def generate_unique_node_label(G):
    existing_labels = set(G.nodes())
    new_label = 1
    while new_label in existing_labels:
        new_label += 1
    return new_label

# Example usage:
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])  # Add some initial nodes

unique_label = generate_unique_node_label(G)
print(f"Unique node label generated: {unique_label}")
