import json
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge('1', '2')
G.add_edge('2', '3')

# NetworkX provides a method to convert to dictionary
data = nx.node_link_data(G)

# Convert dictionary to JSON
json_data = json.dumps(data)

print(json_data)
