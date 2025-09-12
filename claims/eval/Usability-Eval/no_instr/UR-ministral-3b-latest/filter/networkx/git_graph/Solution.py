import json
import networkx as nx

def read_graph_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    G = nx.DiGraph()
    for node, attributes in data.items():
        if 'children' in attributes:
            for child in attributes['children']:
                G.add_edge(node, child)

    return G

file_path = 'graph.json'
graph = read_graph_from_json(file_path)
print(graph)
