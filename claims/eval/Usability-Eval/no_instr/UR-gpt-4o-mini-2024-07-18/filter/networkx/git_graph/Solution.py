import networkx as nx
import json

def read_graph_from_jit_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    G = nx.Graph()  # Create a new graph instance

    # Assuming the JSON structure contains 'nodes' and 'edges'
    for node in data['nodes']:
        G.add_node(node['id'], **node.get('attributes', {}))

    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge.get('attributes', {}))

    return G

# Example usage
# graph = read_graph_from_jit_json('path_to_your_file.json')
