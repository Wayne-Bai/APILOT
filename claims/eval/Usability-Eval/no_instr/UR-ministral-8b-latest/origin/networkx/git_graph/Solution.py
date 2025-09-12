import json
import networkx as nx

# Read the graph data from the JSON file
with open('graph_data.json') as f:
    data = json.load(f)

# Create an empty directed graph
graph = nx.DiGraph()

# Add nodes to the graph
for node in data['nodes']:
    graph.add_node(node['id'], attr=node['attribute'])

# Add edges to the graph
for edge in data['edges']:
    graph.add_edge(edge['source'], edge['target'], weight=edge['weight'])

# Print the nodes and edges of the graph
print("Nodes:", graph.nodes(data=True))
print("Edges:", graph.edges(data=True))
