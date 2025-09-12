import networkx as nx
import yaml

def read_yaml_graph(path):
    """
    Read graph in YAML format from path.

    Args:
    path (str): Path to YAML file containing graph data.

    Returns:
    nx.Graph: Graph read from YAML file.
    """
    try:
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)
            try:
                G = nx.Graph()
                if 'nodes' in data:
                    for node in data['nodes']:
                        G.add_node(node)
                if 'edges' in data:
                    for edge in data['edges']:
                        if'source' in edge and 'target' in edge:
                            G.add_edge(edge['source'], edge['target'])
                        elif 'node1' in edge and 'node2' in edge:
                            G.add_edge(edge['node1'], edge['node2'])
                        else:
                            raise ValueError("Invalid edge format in YAML file.")
                return G
            except Exception as e:
                print("Failed to parse YAML graph: ", e)
                return None
    except FileNotFoundError:
        print("File not found at path: ", path)
        return None

# Example usage:
path_to_yaml = 'graph.yaml'
G = read_yaml_graph(path_to_yaml)
if G is not None:
    print("Graph loaded. Nodes:", G.nodes())
    print("Edges:", G.edges())
