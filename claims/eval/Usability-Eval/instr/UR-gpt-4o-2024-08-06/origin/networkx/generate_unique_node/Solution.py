import networkx as nx

def generate_unique_node_label(graph, prefix='node'):
    # Get all existing node labels
    existing_labels = set(graph.nodes)
    
    # Start from 0 and increment to find a unique label
    index = 0
    while True:
        candidate_label = f"{prefix}_{index}"
        if candidate_label not in existing_labels:
            return candidate_label
        index += 1

# Example usage:
G = nx.Graph()
G.add_node('node_0')
G.add_node('node_1')

unique_label = generate_unique_node_label(G)
print("Unique node label:", unique_label) 
