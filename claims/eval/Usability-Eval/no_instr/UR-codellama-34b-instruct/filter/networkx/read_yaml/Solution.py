import networkx as nx
import yaml

# Load the YAML file into a Python object
with open("graph.yml", 'r') as f:
    data = yaml.safe_load(f)

# Create a graph from the loaded data
G = nx.DiGraph()
for node in data["nodes"]:
    G.add_node(node["name"])
    for neighbor in node["neighbors"]:
        G.add_edge(node["name"], neighbor["name"])
