# Import the necessary libraries
import networkx as nx
import json

# Open the JSON file
with open('your_file.json', 'r') as f:
    json_graph = json.load(f)

# Create a graph from json_graph
G = nx.jit_graph(json_graph)
