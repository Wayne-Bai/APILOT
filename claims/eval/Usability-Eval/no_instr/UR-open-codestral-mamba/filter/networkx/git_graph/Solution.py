import networkx as nx
import json

def read_graph_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    G = nx.Graph(data)
    return G

# usage
G = read_graph_from_json('your_json_file.json')
