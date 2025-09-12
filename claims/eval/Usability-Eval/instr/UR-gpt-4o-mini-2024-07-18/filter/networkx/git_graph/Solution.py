import networkx as nx
import json

def read_graph_from_jit_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    G = nx.Graph()

    # Assuming data has 'nodes' and 'links' keys
    for node in data['nodes']:
        G.add_node(node['id'], **node)

    for link in data['links']:
        G.add_edge(link['source'], link['target'], **link)
    
    return G

# Example usage:
# graph = read_graph_from_jit_json('path_to_your_file.json')
