import networkx as nx
import yaml

def read_graph_from_yaml(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            G = nx.Graph()
            for node, edge_info in data.items():
                G.add_node(node)
                for edge in edge_info['edges']:
                    G.add_edge(node, edge['to'], weight=edge['weight'])
            return G

# Example usage
file_path = 'path_to_your_graph.yaml'
graph = read_graph_from_yaml(file_path)