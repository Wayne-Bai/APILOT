import json
import networkx as nx

# Load the graph from a JSON file
with open('graph.json') as f:
    graph = json.load(f)

G = nx.convert_graph(graph)
