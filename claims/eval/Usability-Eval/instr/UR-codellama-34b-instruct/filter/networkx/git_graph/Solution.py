
import json
import networkx as nx

# Read the JIT JSON file
with open("graph.jit", "r") as f:
    data = json.load(f)

# Create a NetworkX DiGraph object from the JSON data
G = nx.DiGraph()
for node in data["nodes"]:
    G.add_node(node["id"], **node["attr"])
for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"], **edge["attr"])
