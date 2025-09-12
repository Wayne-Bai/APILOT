import json
import networkx as nx

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with attributes
G.add_node(1, name="Node 1", value=10)
G.add_node(2, name="Node 2", value=20)
G.add_node(3, name="Node 3", value=30)

# Add edges with attributes
G.add_edge(1, 2, weight=5, label="Edge 1-2")
G.add_edge(2, 3, weight=10, label="Edge 2-3")
G.add_edge(3, 1, weight=15, label="Edge 3-1")

# Store nodes and edges data in a format suitable for conversion to JSON
nodes = []
edges = []

# Extract nodes from the graph
for node in G.nodes(data=True):
    node_info = {
        'id': node[0],
        'attributes': node[1]
    }
    nodes.append(node_info)

# Extract edges from the graph
for edge in G.edges(data=True):
    edge_info = {
        'source': edge[0],
        'target': edge[1]['label'],
        'attributes': edge[2]
    }
    edges.append(edge_info)

# Create JIT JSON object
data = {
    "nodes": nodes,
    "edges": edges
}

# Convert to JSON format
jit_json_str = json.dumps(data, indent=4)

# Print the JSON formatted string
print(jit_json_str)
