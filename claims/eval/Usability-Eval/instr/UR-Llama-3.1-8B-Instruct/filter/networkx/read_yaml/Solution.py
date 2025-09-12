import networkx as nx
import yaml

def read_graph_from_yaml(path):
    """
    Read graph in YAML format from a given path.

    Args:
    path (str): The path to the YAML file containing the graph.

    Returns:
    nx.DiGraph: A directed graph object representing the graph stored in the YAML file.
    """
    with open(path, 'r') as file:
        graph_data = yaml.safe_load(file)
        G = nx.DiGraph()

        # Check if the graph_data is a dictionary
        if isinstance(graph_data, dict):
            # Add nodes
            for node in graph_data.get('nodes', []):
                G.add_node(node['id'], **node.get('attributes', {}))

            # Add edges
            for edge in graph_data.get('edges', []):
                # Assuming edge tuples are in format (source, target)
                source_id = edge['source']
                target_id = edge['target']
                G.add_edge(source_id, target_id)
        else:
            raise ValueError("Invalid graph data. Expected a dictionary.")

    return G
