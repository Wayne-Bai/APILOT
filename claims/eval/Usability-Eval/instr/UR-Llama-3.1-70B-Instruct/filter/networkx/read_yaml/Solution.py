import networkx as nx
import yaml

def read_yaml_graph(path):
    """
    Read graph in YAML format from path.

    Args:
    path (str): Path to the YAML file containing the graph.

    Returns:
    nx.Graph: A NetworkX graph object.
    """
    with open(path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # Create a new empty graph
    G = nx.Graph()

    # Add nodes
    for node, node_data in data['nodes'].items():
        G.add_node(node, **node_data)

    # Add edges
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge.get('data', {}))

    return G

# Example usage
path_to_yaml_file = 'path_to_your_yaml_file.yaml'  # replace with your yaml file path
G = read_yaml_graph(path_to_yaml_file)

# Print nodes and edges
print("Nodes:")
print(G.nodes(data=True))
print("\nEdges:")
print(G.edges(data=True))
