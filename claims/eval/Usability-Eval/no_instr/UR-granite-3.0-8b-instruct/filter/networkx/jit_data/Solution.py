import json
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")

# Convert the graph to a JSON format
json_data = nx.json_graph.node_link_data(G)

# Print the JSON data
print(json.dumps(json_data, indent=4))
