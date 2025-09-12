import networkx as nx
import json

# Read graph from JIT JSON
with open('graph.json', 'r') as f:
    graph = nx.read_json(f)

# Now you can use the 'graph' object for further operations
