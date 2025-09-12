import networkx as nx
import json

def read_jit_json_file(file_path):
    """
    Reads a graph from a JIT JSON file.

    Args:
        file_path (str): The path to the JIT JSON file.

    Returns:
        G (networkx.DiGraph): The directed graph read from the JIT JSON file.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    G = nx.DiGraph()

    # Add nodes
    for node in data['nodes']:
        G.add_node(node['id'], **node)

    # Add edges
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge)

    return G

# Example usage:
file_path = 'path_to_your_jit_json_file.json'  # replace with your file path
G = read_jit_json_file(file_path)
print(G.nodes(data=True))
print(G.edges(data=True))
