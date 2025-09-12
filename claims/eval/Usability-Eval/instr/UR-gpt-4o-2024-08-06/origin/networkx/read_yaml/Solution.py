import networkx as nx
import yaml

def read_graph_from_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    G = nx.Graph()

    # Adding nodes
    for node in yaml_data.get('nodes', []):
        # Assuming 'id' is the key for node identifier
        node_id = node['id']
        node_attrs = {k: v for k, v in node.items() if k != 'id'}
        G.add_node(node_id, **node_attrs)

    # Adding edges
    for edge in yaml_data.get('edges', []):
        # Assuming 'source' and 'target' are the keys for edge identifiers
        source = edge['source']
        target = edge['target']
        edge_attrs = {k: v for k, v in edge.items() if k not in ['source', 'target']}
        G.add_edge(source, target, **edge_attrs)

    return G

# Example usage
yaml_path = 'path_to_yaml_file.yaml'
graph = read_graph_from_yaml(yaml_path)
