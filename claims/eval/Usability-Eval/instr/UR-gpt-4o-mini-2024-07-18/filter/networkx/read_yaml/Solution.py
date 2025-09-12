import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        
    G = nx.Graph()  # Create a new graph
    
    # Adding nodes and edges from the YAML data
    for node in data['nodes']:
        G.add_node(node)
        
    for edge in data['edges']:
        G.add_edge(edge[0], edge[1])
    
    return G

# Example usage
# graph = read_graph_from_yaml('path_to_your_yaml_file.yaml')
