import networkx as nx
import yaml

def read_graph_from_yaml(path):
    """
    Read a graph from a YAML file.
    
    Parameters:
    path (str): The path to the YAML file containing the graph.
    
    Returns:
    G (nx.Graph): The graph represented using networkx.
    """
    
    # Read YAML data from the file
    with open(path, 'r') as f:
        graph_data = yaml.safe_load(f)
    
    # Create a new graph
    G = nx.Graph()
    
    # Get the nodes and edges from the graph data
    nodes = graph_data.get('nodes', [])
    edges = graph_data.get('edges', [])
    
    # Add nodes to the graph
    for node in nodes:
        G.add_node(node)
    
    # Add edges to the graph
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    return G

# Example usage
path_to_yaml_file = 'path_to_your_yaml_file.graph.yaml'
graph = read_graph_from_yaml(path_to_yaml_file)
print(graph.nodes())
print(graph.edges())
