import networkx as nx
import yaml

def write_graph_to_yaml(G, path):
    """
    Writes the graph G to the specified path in YAML format.

    Args:
        G (networkx.Graph): The graph to write.
        path (str): The path where the YAML file will be written.
    """
    # Create a dictionary representation of the graph
    graph_dict = {
        'nodes': [node for node in G.nodes()],
        'edges': [(u, v) for u, v in G.edges()]
    }

    # Write the dictionary to a YAML file
    with open(path, 'w') as file:
        yaml.dump(graph_dict, file, default_flow_style=False)

# Example usage:
if __name__ == "__main__":
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges
    G.add_node('A')
    G.add_node('B')
    G.add_edge('A', 'B')

    # Write the graph to a YAML file
    write_graph_to_yaml(G, 'graph.yaml')
