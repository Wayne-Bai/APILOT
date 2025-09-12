
import json
from networkx import Graph

# read the graph from JIT JSON file
with open('graph.json') as f:
    data = json.load(f)
    G = nx.Graph()
    for node in data['nodes']:
        G.add_node(node['id'])
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])
