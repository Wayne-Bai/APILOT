import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    G = nx.Graph()
    
    if 'nodes' in data:
        for node in data['nodes']:
            G.add_node(node['id'], **node.get('attributes', {}))
    
    if 'edges' in data:
        for edge in data['edges']:
            G.add_edge(edge['source'], edge['target'], **edge.get('attributes', {}))
    
    return G

# Example usage:
# graph = read_graph_from_yaml('path_to_your_yaml_file.yaml')
