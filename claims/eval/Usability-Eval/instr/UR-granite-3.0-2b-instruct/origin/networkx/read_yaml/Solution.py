import networkx as nx
import yaml

# Read graph from YAML format
with open('graph.yaml', 'r') as file:
    graph = nx.read_yaml(file)

# Print the graph
print(graph.nodes())
print(graph.edges())
