import yaml
import networkx as nx

# Read graph from YAML format
with open('graph.yaml', 'r') as file:
    graph_data = yaml.safe_load(file)

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes and edges from the graph data
for node, edges in graph_data.items():
    for edge in edges:
        G.add_edge(node, edge)
