import json
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge('node1', 'node2', weight=0.5)
G.add_edge('node2', 'node3', weight=0.7)

# Convert the graph to JSON
graph_json = json.dumps(nx.node_link_data(G))

# Output the JSON
print(graph_json)
