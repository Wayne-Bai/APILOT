import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
    with open(file_path, 'r') as file:
        graph_data = yaml.safe_load(file)

    graph = nx.DiGraph() if graph_data.get('directed') else nx.Graph()

    for node, neighbors in graph_data['nodes'].items():
        graph.add_node(node)
        for neighbor, edge_data in neighbors.items():
            graph.add_edge(node, neighbor, **edge_data)

    return graph
