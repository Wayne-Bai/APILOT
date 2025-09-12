import networkx as nx

def generate_unique_node_label(node_list):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes to the graph
    for node in node_list:
        G.add_node(node)

    # Generate unique node labels
    labels = {node: f"node_{i}" for i, node in enumerate(G.nodes)}

    return labels
