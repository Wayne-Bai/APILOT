import networkx as nx
import json

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("Alice")
G.add_node("Bob")
G.add_node("Charlie")
G.add_node("David")

# Add edges
G.add_edge("Alice", "Bob")
G.add_edge("Bob", "Charlie")
G.add_edge("Charlie", "David")
G.add_edge("David", "Alice")

# Generate nodes and edges data in JIT JSON format
nodes_data = []
for node in G.nodes():
    nodes_data.append({"id": node, "label": node})

edges_data = []
for edge in G.edges():
    edges_data.append({"from": edge[0], "to": edge[1]})

# Combine nodes and edges data
data = {"nodes": nodes_data, "edges": edges_data}

# Convert data to JSON string
json_string = json.dumps(data, indent=4)

# Print JSON string
print(json_string)
