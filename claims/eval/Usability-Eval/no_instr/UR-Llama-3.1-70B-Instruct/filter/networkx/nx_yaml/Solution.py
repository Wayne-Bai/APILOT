import networkx as nx
import yaml

def graph_to_yaml(graph, filename):
    """
    Writes a NetworkX graph to a YAML file.

    Args:
    graph (networkx.Graph): The graph to write.
    filename (str): The filename of the YAML file.
    """
    data = nx.to_dict_of_dicts(graph)
    with open(filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def yaml_to_graph(filename):
    """
    Reads a YAML file and returns a NetworkX graph.

    Args:
    filename (str): The filename of the YAML file.

    Returns:
    networkx.Graph: The graph read from the YAML file.
    """
    with open(filename, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    graph = nx.from_dict_of_dicts(data)
    return graph

# Create a new graph
G = nx.Graph()

# Add nodes and edges
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")

# Write the graph to a YAML file
graph_to_yaml(G, "graph.yaml")

# Read the graph from the YAML file
read_G = yaml_to_graph("graph.yaml")

# Print the nodes and edges of the read graph
print("Nodes:", read_G.nodes())
print("Edges:", read_G.edges())
