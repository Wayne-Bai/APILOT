import networkx as nx
import json

# Load the JSON data
with open('graph_data.json', 'r') as f:
    data = json.load(f)

# Create an empty graph
G = nx.Graph()

# Add nodes
for node in data['nodes']:
    G.add_node(node['id'], attr_dict=node)

# Add edges
for edge in data['edges']:
    # Check if the edge has additional attributes
    if 'attr_dict' in edge:
        G.add_edge(edge['source'], edge['target'], attr_dict=edge['attr_dict'])
    else:
        G.add_edge(edge['source'], edge['target'])

# Now you can use NetworkX functions to manipulate and analyze the graph data
# For example, you can print the graph's number of nodes and edges
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
