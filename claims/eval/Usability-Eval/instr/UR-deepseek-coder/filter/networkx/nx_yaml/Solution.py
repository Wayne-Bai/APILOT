import networkx as nx
import yaml

def graph_to_yaml(graph, file_path):
    data = {
        'nodes': list(graph.nodes(data=True)),
        'edges': list(graph.edges(data=True))
    }
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def yaml_to_graph(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    graph = nx.Graph()
    for node in data['nodes']:
        graph.add_node(node[0], **node[1])
    for edge in data['edges']:
        graph.add_edge(edge[0], edge[1], **edge[2])
    
    return graph

# Example usage:
# G = nx.Graph()
# G.add_edge(1, 2, weight=0.5)
# G.add_node(3, color='red')
# graph_to_yaml(G, 'graph.yaml')
# new_graph = yaml_to_graph('graph.yaml')
