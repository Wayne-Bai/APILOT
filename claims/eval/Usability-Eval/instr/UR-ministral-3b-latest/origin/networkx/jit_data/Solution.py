import networkx as nx
import json

# Create a new empty graph
G = nx.Graph()

# Add nodes and edges
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# Extract graph data to dictionary
graph_data = json.dumps(dict(G), default=str)

# Print the graph data in JIT JSON format
print(graph_data)
