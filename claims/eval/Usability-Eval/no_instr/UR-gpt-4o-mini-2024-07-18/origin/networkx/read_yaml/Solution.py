import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    graph = nx.Graph()
    
    # Assuming 'nodes' and 'edges' are keys in the YAML file
    for node in data.get('nodes', []):
        graph.add_node(node)
        
    for edge in data.get('edges', []):
        graph.add_edge(edge[0], edge[1])
    
    return graph

# Example usage:
# graph = read_graph_from_yaml('path/to/graph.yaml')
