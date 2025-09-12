
import networkx as nx
import json

# Read the JIT JSON file
with open('graph.jit', 'r') as f:
 data = json.load(f)

# Create a new graph
G = nx.Graph()

# Add nodes and edges to the graph
for node_id, node_data in data['nodes'].items():
 G.add_node(node_id, **node_data)

for edge_id, edge_data in data['edges'].items():
 G.add_edge(edge_data['source'], edge_data['target'], **edge_data)
